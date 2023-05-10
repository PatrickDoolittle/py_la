
'''
Matrix Object, formed by a list of column vectors.
String representation prints the matrix line by line with each line representing a row.
'''

from Vector import Vector, vectorProjection, dot, orthogonal
from typing import List


class Matrix:
    def __init__(self, vectors: List[Vector], transpose=False):
        if not isinstance(vectors, List):
            raise TypeError("matrix must be formed of a list of vectors")
        if not all(isinstance(x, Vector) for x in vectors):
            raise TypeError("List must be made up of Vectors")
        if len(vectors) == 0:
            raise ValueError("Matrix must have at least one vector")
        self.vectors = vectors
        if transpose == True:
            self.vectors = self.transpose().vectors

    def __len__(self):
        return len(self.vectors)
    
    def __eq__(self, operand:"Matrix"):
        if not isinstance(operand, Matrix):
            raise TypeError("Operand must be a matrix")
        if self.vectors == operand.vectors:
            return True
        else:
            return False
    
    def __getitem__(self,indices):
        if isinstance(indices, int):
            return self.vectors[indices]
        
    def __setitem__(self, indice, value):
        if isinstance(value, Vector):
            self.vectors[indice] = value
        elif not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("Matrix elements must be numbers")
        elif not isinstance(indice, int):
            raise TypeError("Matrix indices must be integers")
        elif indice >= len(self):
            raise IndexError("Index out of range")
        else:
            self.vectors[indice] = value
    
    def __str__(self):
        print(f"{len(self[0])}x{len(self)} Matrix: ")
        row_self = self.transpose()
        return "\n".join([str(x) for x in row_self.vectors])

    def __add__(self, operand: "Matrix"):
        if not isinstance(operand, Matrix):
            raise TypeError("Operand must be a matrix")
        new_vectors = []
        for i in range(len(self)):
            new_vectors.append(self[i] + operand[i])
        return Matrix(new_vectors)
    
    def __sub__(self, operand: "Matrix"):
        if not isinstance(operand, Matrix):
            raise TypeError("Operand must be a matrix")
        new_vectors = []
        for i in range(len(self)):
            new_vectors.append(self[i] - operand[i])
        return Matrix(new_vectors)


    def __mul__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand must be a vector")
        # Columns of matrix must equal rows of vector
        if len(self) != len(operand):
            raise ValueError("Matrix and vector must be of same length")
        new_vector = []
        for i in range(len(self)):
            new_vector.append(dot(self.transpose()[i], operand))
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
    
    def scale(self, scalar):
        if not isinstance(scalar, float) and not isinstance(scalar, int):
            raise TypeError("Scalar must be a number")
        new_vectors = []
        for i in range(len(self)):
            new_vectors.append(self[i] * scalar)
        return Matrix(new_vectors)

    def swap(self, i, j):
        #  Returns a new_matrix with the i and jth rows swapped
        copied_self = self.vectors.copy()
        copied_self[i], copied_self[j] = copied_self[j], copied_self[i]
        return Matrix(copied_self)
    
    def transpose(self):
        new_vectors = []
        for j in range(len(self[0])):
            row = []
            for i in range(len(self)):
                row.append(self[i][j])
            new_vectors.append(Vector(row))
        return Matrix(new_vectors)
    
    def row_echelon(self):
        # Returns row-echelon form of self, rows are sorting in ascending amount of leading zeros
        row_self = self.transpose()
        for i in range(len(row_self)):
            #Skip zero columns
            if self[i].is_zero():
                continue

            #Find first row with a non-zero element in column i, and s
            for j in range(i + 1, len(row_self)):
                if row_self[j][i] != 0:
                    row_self = row_self.swap(i, j)
                    break
 
            # Iterate over all *subsequent* rows except row i reducing them
            for k in range(i+1, len(row_self)):
                if k == i:
                    continue
                if row_self[k][i] == 0:
                    continue
                row_self[k] = row_self[k] - row_self[i].scale(row_self[k][i] / row_self[i][i])

        return row_self.transpose()

    def row_reduce(self):
        #Return transpose of self because row-operations are not defined
        row_self = self.transpose()
        for i in range(len(row_self)):
            #if row[i] is all zeros, skip it
            if row_self[i].is_zero():
                continue

            #Find first non-zero element in self[i]
            for j in range(i+1, len(row_self[0])):
                if row_self[i][j] != 0:
                    row_self = row_self.swap(i, j)
                    break

            # Now we know that row i has a non-zero element in column i, divide X^T[i] by that element
            row_self[i] = row_self[i].scale(1/row_self[i][i])

            # Iterate over all rows except row i
            for k in range(0, len(row_self)):
                if k == i:
                    continue
                row_self[k] = row_self[k] - row_self[i].scale(row_self[k][i])
        return row_self.transpose()

                

'''
Need to implement gaussian elimination to find number of linear independent vectors
before trying GS process
'''

#    def gramSchmidt(self):
#        '''
#        Returns the gram schmidt orthogonalization of the matrix A
#        '''
#        e_hat = self[0].unitize()
#        hat_vectors  = [e_hat]
#        for i in range(1,len(self)):
#            new_hat = self[i] - vectorProjection(self[i], e_hat)
#            for j in range(1, len(hat_vectors)):
#                new_hat = new_hat - vectorProjection(self[i], hat_vectors[j])
#            hat_vectors.append(new_hat.unitize())
#        new_matrix = Matrix(hat_vectors)
#        print(new_matrix)
#        for i in range(len(new_matrix)):
#            for j in range(i+1,len(new_matrix)):
#                if i != j:
#                    if not orthogonal(new_matrix[i], new_matrix[j]):
#                        raise ValueError("Gram schmidt failed to produce orthogonal vectors.")
#        return new_matrix