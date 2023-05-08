'''
A Linear Algebra Implementation to solve a simple linear regression problem
'''


from Vector import Vector, vectorProjection
from Matrix import Matrix
from typing import List


def linear_projection(data: List[tuple]):
    dependent_vector_elements = [x[1] for x in data]
    dependent_vector = Vector(dependent_vector_elements)
    independent_vector_elements = [x[0] for x in data]
    independent_vector = Vector(independent_vector_elements)    

    constant_column = [1 for i in range(len(data))]
    constant_vector = Vector(constant_column)
    design_matrix = Matrix([constant_vector, independent_vector])
    design_hat = design_matrix.gramSchmidt()
    y_hat = vectorProjection(dependent_vector, design_hat[0]) + vectorProjection(dependent_vector, design_hat[1])
    return y_hat


'''
Unit test for the linear regression function
'''
print("Test for calculating y-hat as sum of vector projections on column space of design matrix.")
data = [(1,2),(2,4),(3,5),(4,8)]
data_vectors = [Vector(list(x)) for x in data]
v = linear_projection(data)
print(str(v))
