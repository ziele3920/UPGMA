from ete3 import Tree
import numpy as np

import Matrix
import UPGMA

dataMatrix = np.genfromtxt("cc.csv", dtype=float, delimiter=',', skip_header=1)
names = np.genfromtxt("cc.csv", dtype=float, delimiter=',', names=True).dtype.names
matrix = Matrix.Matrix(names, dataMatrix)
minIndex = matrix.getMinIndex()
#UPGMA.calculateTree(distanceMartix)

t = Tree("((kotek, (upa, pumpa)), (a,b),(dupa, (kupa, kal)));")
t.show()

