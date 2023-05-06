'''
File to hold all the functions which operate on matrices
'''

from Matrix import Matrix
from Vector import Vector
from VectorOperations import *

def gramSchmidt(A: Matrix):
    '''
    Returns the gram schmidt orthogonalization of the matrix A
    '''
    first_base = A[0].unitize()
    new_vectors = [first_base]
    for i in range(1,len(A)):
        new_vector = A[i] - vectorProjection(A[i], first_base)
        new_vector = new_vector.unitize()
        new_vectors.append(new_vector)
    return Matrix(new_vectors)

#Quick unit test of gramSchmidt
A = Matrix([Vector([1,1,0]), Vector([1,0,1]), Vector([0,1,1])])
print("A: " + str(A))
print("gramSchmidt(A): " + str(gramSchmidt(A)))

