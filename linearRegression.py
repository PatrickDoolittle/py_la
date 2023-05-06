'''
A Linear Algebra Implementation to solve a simple linear regression problem
'''


from Vector import Vector
from VectorOperations import *
from Matrix import Matrix
from typing import List
from Visualization import plot_vectors


def linear_projection(data: List[tuple]):
    dependent_vector_elements = [x[1] for x in data]
    dependent_vector = Vector(dependent_vector_elements)
    print("Showing dependent vector")
    print(str(dependent_vector))
    independent_vector_elements = [x[0] for x in data]
    independent_vector = Vector(independent_vector_elements)    

    constant_column = [1 for i in range(len(data))]
    constant_vector = Vector(constant_column)
    design_matrix = Matrix([constant_vector, independent_vector])
    y_hat = vectorProjection(dependent_vector, design_matrix[0]) + vectorProjection(dependent_vector, design_matrix[1])
    print(str(y_hat))
    return y_hat







'''
Unit test for the linear regression function
'''
print("Test for calculating y-hat as sum of vector projections on column space of design matrix.")
data = [(1,2),(2,4),(3,5),(4,8)]
data_vectors = [Vector(list(x)) for x in data]
#Plot the data vectors
#plot_vectors(data_vectors)
v = linear_projection(data)
print(str(v))
