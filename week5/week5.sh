blastn -remote -query week5_query.fa -db nr -outfmt "6 sseqid sseq" -evalue 0.0001 -out output.out -max_target_seqs 1000


sed 's/-//g' blast_out.tab | sed 's/^/>/'  >  new_blast_output.tab

awk '{print $1"\n"$3}' < new_blast_output.tab > new_blast_output.fa

transeq new_blast_output.fa translation.out

mafft translation.out > aa_alignment.out

./back_nt.py new_blast_output.fa aa_alignment.out 