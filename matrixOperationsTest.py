from Matrix import Matrix
from Vector import Vector
from MatrixOperations import *
from VectorOperations import *



'''
Check gramschmidt process fails when column vectors are not linearly independent
'''
A = Matrix([Vector([1,1,0]), Vector([1,0,1]), Vector([1,0,1])])
print("A: " + str(A))
try:
    B = gramSchmidt(A)
except ValueError as e:
    print("Pass")

'''
Check gramschmidt process creates orthonormal basis set if column vectors are linearly independent of a 4x4 matrix
'''

A = Matrix([Vector([5,0,0,0]), Vector([0,3,0,0]), Vector([0,0,7,0]), Vector([0,0,0,1])])
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
                

