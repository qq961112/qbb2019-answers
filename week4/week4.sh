plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pca 2 --allow-extra-chr --allow-no-sex --mind 

./pca_generelatedness.py plink.eigenvec 

plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf --freq --allow-extra-chr --allow-no-sex

./afspectrum.py plink.frq

./transform_id.py BYxRM_PhenoData.txt > phenotype.txt

plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pheno phenotype.txt --allow-extra-chr --allow-no-sex --assoc --all-pheno 

./manhattan.py phenotype.txt 