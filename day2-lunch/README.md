#a
head -n 40000 SRR072893.fastq > SRR072893.10k.fastq 
wc SRR072893.10k.fastq

#b
fastqc SRR072893.10k.fastq

#c
hisat2 -p 4 -x BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam

#d
samtools view -S -b SRR072893.10k.sam > SRR072893.10k.bam
samtools sort -@ 4 SRR072893.10k.bam -o SRR072893.10k.sorted.bam
samtools index -b SRR072893.10k.sorted.bam 

#e
stringtie SRR072893.10k.sorted.bam -e -B -p 4 -G BDGP6.Ensembl.81.gtf -o SRR072893.10k.sorted.bam