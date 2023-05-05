
'''
Matrix Object, formed by a list of column vectors, or a list of row vectors (just immediately transpose).
'''

from Vector import Vector
from VectorOperations import *
from typing import List


class Matrix:
    def __init__(self, vectors: List[Vector], transpose=False):
        if not isinstance(vectors, List):
            raise TypeError("matrix must be formed of a list of vectors")
        if not all(isinstance(x, Vector) for x in vectors):
            raise TypeError("List must be made up of Vectors")
        self.vectors = vectors
        if transpose == True:
            self.vectors = self.transpose().vectors

    def __len__(self):
        return len(self.vectors)
    
    def __getitem__(self,indices):
        if isinstance(indices, int):
            return self.vectors[indices]
        if len(indices) != 2:
            raise IndexError("Matrix needs 1 or 2 indices")   
        i1, i2 = indices
        return self.vectors[i1][i2]

    def transpose(self):
        new_vectors = []
        for j in range(len(self[0])):
            row = []
            for i in range(len(self)):
                row.append(self[(i,j)])
            new_vectors.append(Vector(row))
        return Matrix(new_vectors)


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
print(str(A[0][0]))

