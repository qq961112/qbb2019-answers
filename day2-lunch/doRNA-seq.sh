#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq
  hisat2 -p 4 -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort -@ 4 $SAMPLE.sam -o $SAMPLE.sorted.bam
  samtools index $SAMPLE.sorted.bam
  stringtie $SAMPLE.sorted.bam -e -B -p 4 -G $ANNOTATION -o $SAMPLE.sorted.bam
done