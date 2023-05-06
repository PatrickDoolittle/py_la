'''
This file is where I will define visualizations of vectors and linear transformations using matplotlib
'''
import matplotlib.pyplot as plt
from typing import List
from Vector import Vector
from VectorOperations import *
from linearRegression import *

def plot_vector(v: Vector):
    '''
    Plots a 3d vector in 3d space and a 2 or 1 dimensional vector in 2d space
    '''
    if len(v) == 2:
        # Plot a 2d vector
        fig, ax = plt.subplots()
        ax.quiver(0,0, v[0], v[1],angles='xy', scale_units='xy', scale=1)
        max_value = max(v[0], v[1])
        axis_range = max_value + 1
        ax.axis([-axis_range, axis_range, -axis_range, axis_range])
        plt.show()

def plot_vectors(vectors: List[Vector]):
    '''
    Plots a list of vectors in 3d space and a 2 or 1 dimensional vector in 2d space
    '''
    if len(vectors[0]) == 2:
        # Plot a 2d vector
        fig, ax = plt.subplots()
        for v in vectors:
            ax.quiver(0,0, v[0], v[1],angles='xy', scale_units='xy', scale=1)
        max_value = max([max(v) for v in vectors])
        axis_range = max_value + 1
        ax.axis([-axis_range, axis_range, -axis_range, axis_range])
        plt.show()

#Quick test for 2d vector plotting
v = Vector([1,2])
plot_vector(v)

#Test for plotting a list of vectors.
vectors = [Vector([1,2]), Vector([2,3]), Vector([3,4])]
plot_vectors(vectors)
