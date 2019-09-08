#Exercise#1 
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
stringtie SRR072893.10k.sorted.bam -e -B -p 4 -G BDGP6.Ensembl.81.gtf -o Test.gtf

#Exercise#3
grep "gene" SRR072893.sorted.bam| cut -f 1 | uniq -c > day2-lunch-exercise#3.txt

The "grep" command is to select the lines in the .bam that contain the alignments.

The "cut" command and "-f" option is to select the column of chromosomes.

The "uniq" command and "-c" option is to count the numbers of lines of alignments that appears for each chromosome.

"> day2-lunch-exercise#3.txt" is to output the results as a .txt file named day2-lunch-exercise#3.txt. 



#Exercise#4b
"NF" in the awk command line means number of fields, and it can be 12, 13, 20, 21 or 22 for the file SRR072893.sam.

In each line of the .sam file, there are 11 mandatory fields and some tab-seperated optional fields whose number the type of the alignment. All optional fields follow the TAG:TYPE:VALUE format, and tags starting with ‘X’, ‘Y’, or ‘Z’ are for local use. Different alignments may get different numbers of fields due to the locally-defined tags and their features. 

Those lines with 12 fields only contain 1 optional field, YT:Z:UU, which indicates that the read was not part of a pair. 

Lines with 13 fields contain an extra tag, YF, which means they are filtered out.

Lines with 20 fields get tags of AS, XN, XM, XO, XG, NM, MD, YT and NH, suggesting that they are ailgned reads. 

Lines with 21 fields get an extra tag, XS, indicating they are sliced alignments and can be mapped to one of the strand.

Lines with 22 fields get an extra tag other than XS, ZS. The tag marks the alignment of reads that involves SNPs.

<Reference:
(https://www.thegeekstuff.com/2010/01/8-powerful-awk-built-in-variables-fs-ofs-rs-ors-nr-nf-filename-fnr/)
(http://ccb.jhu.edu/software/hisat2/manual.shtml#sam-output)
(https://samtools.github.io/hts-specs/SAMtags.pdf)
(http://samtools.github.io/hts-specs/SAMv1.pdf)>