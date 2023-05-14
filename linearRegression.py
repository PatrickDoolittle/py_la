'''
A Linear Algebra Implementation to solve Linear Regression problems
'''


from Vector import Vector, vectorProjection
from Matrix import Matrix
from typing import List


def orthogonal_projection(data: List[tuple]):
    #For a given set of data points in two variables, returns the orthogonal projection of the dependent variable onto the column space of the design matrix
    dependent_vector_elements = [x[1] for x in data]
    dependent_vector = Vector(dependent_vector_elements)
    independent_vector_elements = [x[0] for x in data]
    independent_vector = Vector(independent_vector_elements)    

    constant_column = [1 for i in range(len(data))]
    constant_vector = Vector(constant_column)
    design_matrix = Matrix([constant_vector, independent_vector])
    print("Design matrix: " + str(design_matrix))
    if design_matrix.rank() != len(design_matrix):
        raise ValueError("Design matrix is not full rank.")
    design_hat = design_matrix.gramSchmidt()
    print("Orthogonalized design matrix: " + str(design_hat))
    y_hat = vectorProjection(dependent_vector, design_hat[0]) + vectorProjection(dependent_vector, design_hat[1])
    return y_hat


'''
Unit test for the linear regression function
'''
print("Test for calculating y-hat as sum of vector projections on column space of design matrix.")
data = [(1,2),(2,4),(3,5),(4,8)]
data_vectors = [Vector(list(x)) for x in data]
v = orthogonal_projection(data)
print("Data: " + str(data))
print("y-hat: " + str(v))

#Test that linear dependent matrix throws error
print("Test for linear dependent matrix.")
data = [(1,2),(2,4),(3,6),(4,8)]
data_vectors = [Vector(list(x)) for x in data]
v = orthogonal_projection(data)

print("Data: " + str(data))
print("y-hat: " + str(v))