from ete3 import Tree
import numpy as np

import Cluster
import Matrix
import UPGMA
from Tree import GraphicalTree

dataMatrix = np.genfromtxt("cc.csv", dtype=float, delimiter=',', skip_header=1)
names = np.genfromtxt("cc.csv", dtype=float, delimiter=',', names=True).dtype.names
clusters = list()

for x in range(0, len(names)):
    clusters.append(Cluster.Cluster(names[x],  None, list([x]), True))

matrix = Matrix.Matrix(clusters, dataMatrix)
mergingList = UPGMA.calculateTree(matrix.distanceMatrix, matrix)

graphicalTree = GraphicalTree()

for pair in mergingList:
    print(pair.cluster1.name + " & " + pair.cluster2.name)
    graphicalTree.addNode(pair.cluster1, pair.cluster2)

t = Tree(graphicalTree.nodes[0].graphicalString + ";")
t.show()


