'''
A Linear Algebra Implementation to solve Linear Regression problems
'''

from Vector import Vector, vectorProjection, dot
from Matrix import Matrix
from typing import List

def design(data: List[tuple]):
    #For a given set of data points in two variables, returns the design matrix and response vector
    dependent_vector_elements = [x[1] for x in data]
    dependent_vector = Vector(dependent_vector_elements)
    independent_vector_elements = [x[0] for x in data]
    independent_vector = Vector(independent_vector_elements)    

    constant_column = [1 for i in range(len(data))]
    constant_vector = Vector(constant_column)
    design_matrix = Matrix([constant_vector, independent_vector])
    return design_matrix, dependent_vector

def orthogonal_projection(data: List[tuple]):
    design_matrix, dependent_vector = design(data)
    print("Design matrix: " + str(design_matrix))
    if design_matrix.rank() != len(design_matrix):
        raise ValueError("Design matrix is not full rank.")
    design_hat = design_matrix.gramSchmidt()
    print("Orthogonalized design matrix: " + str(design_hat))
    y_hat = vectorProjection(dependent_vector, design_hat[0]) + vectorProjection(dependent_vector, design_hat[1])
    return y_hat

def linear_regression(data: List[tuple]):
    design_matrix, dependent_vector = design(data)
    if design_matrix.rank() != len(design_matrix):
        raise ValueError("Design matrix is not full rank.")
    # We know that the vector of linear coffiecients beta = (X^T X)^-1 X^T y
    gram_matrix = (design_matrix.transpose() @ design_matrix)
    gram_matrix_inverse = gram_matrix.inverse() @ design_matrix.transpose()
    return gram_matrix_inverse * dependent_vector

def pearson_correlation(x,y):
    if not all(isinstance(i, Vector) for i in [x,y]):
        raise TypeError("Operand is not a vector.")
    if len(x) != len(y):
        raise ValueError("Vectors of mismatched size")
    x_bar = x.vector_mean()
    x_bar_vector = Vector([x_bar for _ in range(len(x))])
    y_bar = y.vector_mean()
    y_bar_vector = Vector([y_bar for _ in range(len(y))])
    x_centered = x - x_bar_vector
    y_centered = y - y_bar_vector
    return dot(x_centered, y_centered) / (x_centered.modulus() * y_centered.modulus())




'''
Unit test for the linear regression function
'''
print("Test for calculating y-hat as sum of vector projections on column space of design matrix.")
data = [(1,2),(2,4),(3,5),(4,8)]
data_vectors = [Vector(list(x)) for x in data]
v = orthogonal_projection(data)
print("Data: " + str(data))
print("y-hat: " + str(v))

print("Test for calculating linear regression coefficients.")
b = linear_regression(data)
print("Data: " + str(data))
print("Beta: " + str(b))


#Test with data that has a bias term
print("Second test for linear regression coefficients.")
data = [(1,7),(2,9),(3,10),(4,13)]
b = linear_regression(data)
print("Data: " + str(data))
print("Beta: " + str(b))

print("Test for calculating pearson correlation.")
data = [(1,2),(2,4),(3,5),(4,8)]
x = Vector([x[0] for x in data])
y = Vector([x[1] for x in data])
print("Data: " + str(data))
print("Pearson correlation: " + str(pearson_correlation(x,y)))