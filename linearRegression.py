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

def linear_regression(data: List[tuple]):
    #For a given set of data points in two variables, returns the coefficients of the linear regression model
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
    # We know that the vector of linear coffiecients beta = (X^T X)^-1 X^T y
    gram_matrix = (design_matrix.transpose() @ design_matrix)
    gram_matrix_inverse = gram_matrix.inverse() @ design_matrix.transpose()
    return gram_matrix_inverse * dependent_vector


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
