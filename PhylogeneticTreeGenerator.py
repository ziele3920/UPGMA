from ete3 import Tree
import numpy as np

import Cluster
import Matrix
import UPGMA

dataMatrix = np.genfromtxt("cc.csv", dtype=float, delimiter=',', skip_header=1)
names = np.genfromtxt("cc.csv", dtype=float, delimiter=',', names=True).dtype.names
clusters = list()

for x in range(0, len(names)):
    clusters.append(Cluster.Cluster(names[x],  None))

matrix = Matrix.Matrix(clusters, dataMatrix)
UPGMA.calculateTree(matrix)

t = Tree("((kotek, (upa, pumpa)), (a,b),(dupa, (kupa, kal)));")
t.show()

