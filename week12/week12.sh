#dataset number
#ES_f_mC: SRR1035454
#EpiSC_mC: SRR1035452

conda install bismark sra-tools igv

fastq-dump -X 1000000 --split-files SRR1035454
fastq-dump -X 1000000 --split-files SRR1035452

fastqc SRR1035452_1.fastq
fastqc SRR1035452_2.fastq

bismark_genome_preparation --bowtie2 --verbose /Users/cmdb/qbb2019-answers/week12/Chr19/

bismark --bowtie2 /Users/cmdb/qbb2019-answers/week12/Chr19/ -1 SRR1035454_1.fastq -2 SRR1035454_2.fastq --sam
bismark --bowtie2 /Users/cmdb/qbb2019-answers/week12/Chr19/ -1 SRR1035452_1.fastq -2 SRR1035452_2.fastq --sam

samtools sort -@ 4 SRR1035454_1_bismark_bt2_pe.sam -o SRR1035454_bismark.sorted.bam
samtools index SRR1035454_bismark.sorted.bam

samtools sort -@ 4 SRR1035452_1_bismark_bt2_pe.sam -o SRR1035452_bismark.sorted.bam
samtools index SRR1035452_bismark.sorted.bam

bismark_methylation_extractor --bedgraph --comprehensive SRR1035454_1_bismark_bt2_pe.sam
bismark_methylation_extractor --bedgraph --comprehensive SRR1035452_1_bismark_bt2_pe.sam

igv

./methylation_difference.py SRR1035452_1_bismark_bt2_pe.bedGraph SRR1035454_1_bismark_bt2_pe.bedGraph > methylation_differences.txt