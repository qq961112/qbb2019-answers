#!/usr/bin/env python3

"""
Usage: ./louvain_clustering.py

"""

import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

n_top_genes = 1000


sc.pp.filter_genes(adata, min_counts=1)  # only consider genes with more than 1 count
sc.pp.normalize_per_cell(                # normalize with total UMI count per cell
     adata, key_n_counts='n_counts_all')
filter_result = sc.pp.filter_genes_dispersion(  # select highly-variable genes
    adata.X, flavor='cell_ranger', n_top_genes=n_top_genes, log=False)
adata = adata[:, filter_result.gene_subset] 


sc.pp.normalize_per_cell(adata) 
sc.pp.log1p(adata)               # log transform: adata.X = log(adata.X + 1)
sc.pp.scale(adata)

sc.pp.neighbors(adata)
sc.tl.louvain(adata, resolution=0.3)

sc.tl.rank_genes_groups(adata, 'louvain', groups= 'all', method = 'logreg')
sc.pl.rank_genes_groups(adata, save = "rank_gene_logistic_regression")


sc.tl.rank_genes_groups(adata, 'louvain', groups= 'all', method = 't-test')
sc.pl.rank_genes_groups(adata,  save = "rank_gene_t_test")