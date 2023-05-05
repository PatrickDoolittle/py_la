'''
A Linear Algebra Implementation to solve a simple linear regression problem
'''


from Vector import Vector
from VectorOperations import *
from Matrix import Matrix
from typing import List

def simpleLinearRegression(data: List[tuple]):
    dependent_vector_elements = [x[1] for x in data]
    dependent_vector = Vector(dependent_vector_elements)
    print("Showing dependent vector")
    print(str(dependent_vector))
    independent_vector_elements = [x[0] for x in data]
    independent_vector = Vector(independent_vector_elements)    

    constant_column = [1 for i in range(len(data))]
    constant_vector = Vector(constant_column)
    print("Showing constant vector")
    print(str(constant_vector))
    print("Showing independent_vector")
    print(str(independent_vector))

    independent_hat = independent_vector.scale(1 / independent_vector.modulus())
    constant_hat = constant_vector.scale(1 / constant_vector.modulus() )
    print(f"Constant hat: {str(constant_hat)}")
    print(f"Independent_hat: {str(independent_hat)}")
    design_matrix = Matrix([constant_vector, independent_vector])
    hat_matrix = Matrix([constant_hat, independent_hat])
    #y_hat = vectorProjection(dependent_vector, hat_matrix[0]) + vectorProjection(dependent_vector, hat_matrix[1])
    y_hat = hat_matrix.transpose() * dependent_vector

    return y_hat







'''
Unit test for the linear regression function
'''
print("Test for calculating y-hat as sum of vector projections on column space of design matrix.")
data = [(1,2),(2,4),(3,5),(4,8)]
v = simpleLinearRegression(data)
print(str(v))
