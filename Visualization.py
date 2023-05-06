'''
This file is where I will define visualizations of vectors and linear transformations using matplotlib
'''
import matplotlib.pyplot as plt
from typing import List
from Vector import Vector

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

    elif len(vectors[0]) == 3:
        # Plot a 3d vector
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for v in vectors:
            ax.quiver(0,0,0, v[0], v[1], v[2],arrow_length_ratio=0.1)
        max_value = max([max(v) for v in vectors])
        axis_range = max_value + 1
        ax.set_xlim([-axis_range, axis_range])
        ax.set_ylim([-axis_range, axis_range])
        ax.set_zlim([-axis_range, axis_range])
        plt.show()



