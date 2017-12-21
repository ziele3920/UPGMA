import numpy as np

import Cluster
import Matrix
import UPGMA
from Tree import GraphicalTree

fileName = "cc.csv"
names = np.genfromtxt(fileName, dtype=float, delimiter=',', names=True).dtype.names
dataMatrix = np.genfromtxt(fileName, dtype=float, delimiter=',', skip_header=1)
clusters = Cluster.generateSingleClustersList(names)
matrix = Matrix.Matrix(clusters, dataMatrix)
mergingList = UPGMA.calculateTree(matrix)
graphicalTree = GraphicalTree(mergingList)
graphicalTree.showTree()




