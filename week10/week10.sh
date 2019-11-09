wget "https://www.dropbox.com/s/7hxh7f61756vc4k/hema_data.txt"

./heatmap.py hema_data.txt

./dendrogram.py hema_data.txt

./k_means.py hema_data.txt

./differentially_expressed_genes.py hema_data.txt