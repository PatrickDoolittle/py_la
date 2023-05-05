from Vector import Vector
from VectorOperations import *
from Matrix import Matrix

'''
Unit test for Matrix module
'''
v1 = Vector([1,2,3])
v2 = Vector([4,5,6])
v3 = Vector([7,8,9])
vectors = [v1,v2,v3]
print("Matrix initialization test")
try:
    A = Matrix(vectors)
except Exception as e:
    raise Exception("fail")

A = Matrix(vectors)
print("pass\n")

print("Index test")
print(str(A[1][1]))

