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
    e_hat = A[0].unitize()
    hat_vectors  = [e_hat]

    for i in range(1,len(A)):
        new_hat = A[i] - vectorProjection(A[i], e_hat)
        for j in range(1, len(hat_vectors)):
            new_hat = new_hat - vectorProjection(A[i], hat_vectors[j])
        hat_vectors.append(new_hat.unitize())

    return Matrix(hat_vectors)

'''
Write a unit test for the gramSchmidt function
'''
print("Testing gramSchmidt function creates a matrix with orthonormal columns using a 4x4 matrix whose columns are not linearly independent.")

A = Matrix([Vector([1,1,0,0]), Vector([1,0,1,0]), Vector([1,0,0,1]), Vector([0,1,1,1])])
print("A: " + str(A))
B = gramSchmidt(A)
print("B: " + str(B))
print("Showing that the columns of B are unitized and orthonormal.")
print("Showing moduli")
for i in range(len(B)):
    print(str(B[i].modulus()))
print("Showing that each column vector is orthonormal to each other column vector.")
for i in range(len(B)):
    for j in range(i+1,len(B)):
            if i != j:
                print(i,j)
                print(orthogonal(B[i], B[j]))
                
