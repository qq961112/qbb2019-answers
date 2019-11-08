wget "https://raw.githubusercontent.com/bxlab/qbb2019/master/data/ER4_peaks.narrowPeak"

conda install meme

wget http://hgdownload.soe.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz

cp ../week6/chr19.fa

sort -n -k 5 -r ER4_peaks.narrowPeak | head -100 > ER4_peaks_sorted.narrowPeak

bedtools getfasta -fi chr19.fa -bed ER4_peaks_sorted.narrowPeak > ER4_chr19_sequence.bed

meme-chip -meme-maxw 20 ER4_chr19_sequence.bed

tomtom memechip_out/combined.meme  JASPAR_CORE_2016.meme

mate density_plot.py

./density_plot.py memechip_out/fimo_out_1/fimo.tsv 