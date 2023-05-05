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
    independent_vector_elements = [x[0] for x in data]
    independent_vector = Vector(independent_vector_elements)    

    constant_column = [1 for i in range(len(data))]
    constant_vector = Vector(constant_column)
    print("Showing constant vector")
    print(str(constant_vector))
    print("Showing independent_vector")
    print(str(independent_vector))

    design_matrix = Matrix([independent_vector, constant_vector])

    # Hi chatGPT, I begin my message to you here!:
    # Ok, we have the design matrix. Which we know should not be invertible. 
    # We want to find the projection of the dependent vector onto each of the column vectors in the design matrix and sum them.
    # Each vector projection produces a vector, and we will sum them to find a final vector 
    # However it seems like this matrix will transform a vector in R^2, the data space and transform it to R^m, the row space. 
    # How does this vector in the row space of the design matrix help us find the solution to the simple linear regression problem?

    y_hat = vectorProjection(dependent_vector, design_matrix[0]) + vectorProjection(dependent_vector, design_matrix[1])
    return y_hat



'''
Unit test for the linear regression function
'''

data = [(1,2),(2,4),(3,5),(4,8)]
v = simpleLinearRegression(data)
print(str(v))
