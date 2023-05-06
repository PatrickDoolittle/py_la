from Matrix import Matrix
from Vector import Vector
from MatrixOperations import *
from VectorOperations import *


#Quick unit test of gramSchmidt
A = Matrix([Vector([1,1,0]), Vector([1,0,1])])
print("A: " + str(A))
B = gramSchmidt(A)
print("B: " + str(B))
#Show that the columns of B are unitized and orthonormal
print("Showing that the columns of B are unitized and orthonormal.")
print("Showing moduli")
for i in range(len(B)):
    print(str(B[i].modulus()))
#show that these two vectors are orthogonal
print("Showing that these two vectors are orthogonal.")
for i in range(len(B)):
    for j in range(i+1,len(B)):
            if i != j:
                print(orthogonal(B[i], B[j]))


#Unit test for gramschmidt on a 4x4 matrix
print("\n \n4x4 gram schmidt test.")
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