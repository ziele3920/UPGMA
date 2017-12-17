from ete3 import Tree
import numpy as np

import Cluster
import Matrix
import UPGMA

dataMatrix = np.genfromtxt("cc.csv", dtype=float, delimiter=',', skip_header=1)
names = np.genfromtxt("cc.csv", dtype=float, delimiter=',', names=True).dtype.names
clusters = tuple([Cluster.Cluster(names[0],  None)])

for x in range(0, len(names)):
    clusters = clusters + Cluster.Cluster(names[x],  None)

matrix = Matrix.Matrix(names, dataMatrix)
UPGMA.calculateTree(matrix)

t = Tree("((kotek, (upa, pumpa)), (a,b),(dupa, (kupa, kal)));")
t.show()

