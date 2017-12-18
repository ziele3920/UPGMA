from ete3 import Tree
import numpy as np

import Cluster
import Matrix
import UPGMA

dataMatrix = np.genfromtxt("cc.csv", dtype=float, delimiter=',', skip_header=1)
names = np.genfromtxt("cc.csv", dtype=float, delimiter=',', names=True).dtype.names
clusters = list()

for x in range(0, len(names)):
    clusters.append(Cluster.Cluster(names[x],  None, list([x]), True))

matrix = Matrix.Matrix(clusters, dataMatrix)
mergingList = UPGMA.calculateTree(matrix.distanceMatrix, matrix)

treeStringList = list()
for pair in mergingList:
    print(pair.cluster1.name + " & " + pair.cluster2.name)
    tmps = ""
    if pair.cluster1.isSingle:
        tmps = "(" + pair.cluster1.name + ", "
    else
        
    if pair.cluster2.isSingle:
        tmps += pair.cluster2.name + ")"
    treeStringList.append(tmps)

t = Tree("(Tuna, ((Dog, (Monkey, Man)), (Chicken, Turtle)));")
t.show()

