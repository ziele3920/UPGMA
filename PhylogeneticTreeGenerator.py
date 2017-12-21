import numpy as np

import Cluster
import Matrix
import UPGMA
from Tree import GraphicalTree

dataMatrix = np.genfromtxt("cc.csv", dtype=float, delimiter=',', skip_header=1)
names = np.genfromtxt("cc.csv", dtype=float, delimiter=',', names=True).dtype.names
clusters = Cluster.generateSingleClustersList(names)
matrix = Matrix.Matrix(clusters, dataMatrix)
mergingList = UPGMA.calculateTree(matrix.distanceMatrix, matrix)
graphicalTree = GraphicalTree(mergingList)
graphicalTree.showTree()




