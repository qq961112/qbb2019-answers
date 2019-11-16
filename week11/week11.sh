conda create -n lab-week11 python=3.6 scanpy jupyter

wget " https://bx.bio.jhu.edu/data/cmdb-lab/scrnaseq/neuron_10k_v3_filtered_feature_bc_matrix.h5"

conda activate lab-week11

./filtering.py
 
./louvain_clustering.py

./marker_genes.py

./color_by_marker_genes.py

conda deactivated 