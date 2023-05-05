
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


    def transpose(self):
        new_vectors = []
        for j in range(len(self[0])):
            row = []
            for i in range(len(self)):
                row.append(self[(i,j)])
            new_vectors.append(Vector(row))
        return Matrix(new_vectors)
