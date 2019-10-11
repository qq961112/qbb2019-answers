tar -xf g1e.tar.xz 

wreg http://hgdownload.soe.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz

bowtie2-build chr19.fa CHR19

bowtie2 -x CHR19 -U input_ER4.fastq -S input_ER4.sam 
bowtie2 -x CHR19 -U input_G1E.fastq -S input_G1E.sam 
bowtie2 -x CHR19 -U CTCF_ER4.fastq -S CTCF_ER4.sam 
bowtie2 -x CHR19 -U CTCF_G1E.fastq -S CTCF_G1E.sam

samtools sort -@ 4 input_ER4.sam -o input_ER4.sorted.bam
samtools sort -@ 4 input_G1E.sam -o input_G1E.sorted.bam
samtools sort -@ 4 CTCF_ER4.sam -o CTCF_ER4.sorted.bam
samtools sort -@ 4 CTCF_G1E.sam -o CTCF_G1E.sorted.bam

conda create -n macs2 macs2

source activate macs2

mkdir callpeaks_G1E
mkdir callpeaks_ER4

macs2 callpeak -t CTCF_G1E.sorted.bam -c input_G1E.sorted.bam -f BAM -g 62309240 --outdir callpeaks_G1E
macs2 callpeak -t CTCF_ER4.sorted.bam -c input_ER4.sorted.bam -f BAM -g 62309240 --outdir callpeaks_ER4

cp ./callpeaks_G1E/NA_peaks.narrowPeak ./NA_peaks_G1E.narrowPeak
cp ./callpeaks_ER4/NA_peaks.narrowPeak ./NA_peaks_ER4.narrowPeak

cut -f 1,2,3,4,5,6 NA_peaks_ER4.narrowPeak > NA_peaks_ER4.bed
cut -f 1,2,3,4,5,6 NA_peaks_G1E.narrowPeak > NA_peaks_G1E.bed

bedtools intersect -v -a NA_peaks_G1E.bed -b NA_peaks_ER4.bed > loss_binding.bed
bedtools intersect -v -a NA_peaks_ER4.bed -b NA_peaks_G1E.bed > gain_binding.bed

wget https://www.taylorlab.org/cmdb-lab/Mus_musculus.GRCm38.94_features.bed

bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b NA_peaks_ER4.bed -wa > ER4_CTCF_annotation.txt
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b NA_peaks_G1E.bed -wa > G1E_CTCF_annotation.txt

conda deactivate

./CTCF_annotation_count.py ER4_CTCF_annotation.txt
./CTCF_annotation_count.py G1E_CTCF_annotation.txt

echo "For G1E CTCF sites" > Annotation_counting.out
./CTCF_annotation_count.py G1E_CTCF_annotation.txt >> Annotation_counting.out
echo "For ER4 CTCF sites" >> Annotation_counting.out
./CTCF_annotation_count.py ER4_CTCF_annotation.txt >> Annotation_counting.out


./two_subplot.py G1E_CTCF_annotation.txt ER4_CTCF_annotation.txt loss_binding.bed gain_binding.bed


