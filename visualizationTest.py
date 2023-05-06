'''
Suite of unit test for the Visualization module
'''

from Visualization import *
from Vector import Vector



#Test for plotting a single vector in 2d.
v = Vector([1,2])
plot_vectors([v])

#Test for plotting a list of vectors in 2d.
vectors = [Vector([1,2]), Vector([2,3]), Vector([3,4])]
plot_vectors(vectors)

#Test for plotting a single vector in 3d
v = Vector([1,2,3])
plot_vectors([v])