#!/usr/bin/env python3

"""
Usage: ./filtering.py

"""

import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

n_top_genes = 1000


sc.pp.normalize_per_cell(adata)          # renormalize after filtering
sc.pp.log1p(adata)               # log transform: adata.X = log(adata.X + 1)
sc.pp.scale(adata)
sc.tl.pca(adata, n_comps=50)
sc.pl.pca(adata, title = "pre-filtering", save = "before_filtering")

adata1 = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata1.var_names_make_unique()
sc.pp.filter_genes(adata1, min_counts=1)  # only consider genes with more than 1 count
sc.pp.normalize_per_cell(                # normalize with total UMI count per cell
     adata1, key_n_counts='n_counts_all')
filter_result = sc.pp.filter_genes_dispersion(  # select highly-variable genes
    adata1.X, flavor='cell_ranger', n_top_genes=n_top_genes, log=False)
adata1 = adata1[:, filter_result.gene_subset]     # subset the genes


sc.pp.normalize_per_cell(adata1)          # renormalize after filtering
sc.pp.log1p(adata1)               # log transform: adata.X = log(adata.X + 1)
sc.pp.scale(adata1)

sc.tl.pca(adata1, n_comps=50)
sc.pl.pca(adata1, title = 'post-filtering', save = "after_filtering")
# sc.pl.pca_loadings(adata)