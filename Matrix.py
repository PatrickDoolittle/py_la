
'''
Matrix Object, formed by a list of column vectors, or a list of row vectors (just immediately transpose).
'''

from Vector import Vector, vectorProjection, dot, orthogonal
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
        
    def __str__(self):
        print(f"{len(self[0])}x{len(self)} Matrix: ")
        return "\n".join([str(x) for x in self.vectors])

    def __mul__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand must be a vector")
        if len(self) != len(operand):
            raise ValueError("Matrix and vector must be of same length")
        new_vector = []
        for i in range(len(self)):
            new_vector.append(dot(self.transpose()[i], operand))
        print("__mul__ returning vector: " + str(new_vector))
        return Vector(new_vector)
    
    def __matmul__(self, operand:"Matrix"):
        if not isinstance(operand, Matrix):
            raise TypeError("Operand must be a matrix")
        if len(self) != len(operand[0]):
            raise ValueError("Columns of left matrix must equal rows of right matrix")
        new_columns = []
        for i in range(len(operand)):
            new_column = []
            for j in range(len(self[0])):
                new_column.append(dot(operand[i], self.transpose()[j]))
            new_columns.append(Vector(new_column))
        return Matrix(new_columns)

    def transpose(self):
        new_vectors = []
        for j in range(len(self[0])):
            row = []
            for i in range(len(self)):
                row.append(self[i][j])
            new_vectors.append(Vector(row))
        return Matrix(new_vectors)
    
    def gramSchmidt(self):
        '''
        Returns the gram schmidt orthogonalization of the matrix A
        '''
        e_hat = self[0].unitize()
        hat_vectors  = [e_hat]
        for i in range(1,len(self)):
            new_hat = self[i] - vectorProjection(self[i], e_hat)
            for j in range(1, len(hat_vectors)):
                new_hat = new_hat - vectorProjection(self[i], hat_vectors[j])
            hat_vectors.append(new_hat.unitize())
        new_matrix = Matrix(hat_vectors)
        for i in range(len(new_matrix)):
            for j in range(i+1,len(new_matrix)):
                if i != j:
                    if not orthogonal(new_matrix[i], new_matrix[j]):
                        raise ValueError("Gram schmidt failed to produce orthogonal vectors.")
        return new_matrix