
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
        if all([self[i] == operand[i] for i in range(len(self))]):
            return True
        else:
            return False
    
    def __getitem__(self,indices):
        if isinstance(indices, int):
            return self.vectors[indices]
        
    def __setitem__(self, indice, value):
        if isinstance(value, Vector):
            self.vectors[indice] = value
        else:  
            raise TypeError("Value must be a vector")
    
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


    def __mul__(self, operand):
        # Return a linear combination of the column vector where the scalar of each column is the corresponding element of the operand vector
        if isinstance(operand, Vector):
            if len(self) != len(operand):
                raise ValueError("Number of columns in Matrix must match elements of Vector")
            new_vector = self[0].scale(operand[0])
            for i in range(1,len(self)):
                new_vector += self[i].scale(operand[i])
            return new_vector
        elif isinstance(operand, int) or isinstance(operand,float):
            new_vectors = [self[i]*operand for i in range(len(self))]
            return Matrix(new_vectors)
        else:
            raise TypeError("Operand must be a Vector or Scalar")


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
        #  Returns a new_matrix with the i and jth columns swapped, typically a row operation (performed on the transpose)
        copied_self = self.vectors.copy()
        copied_self[i], copied_self[j] = copied_self[j], copied_self[i]
        return Matrix(copied_self)
    
    def transpose(self):
        # Returns the transpose of a matrix. This function takes iterates over the rows len(self[0]) of the matrix collecting their elements (len(self)) into Vectors
        # Which the transpose function can then use to create a new matrix
        new_vectors = []
        for j in range(len(self[0])):
            row = []
            for i in range(len(self)):
                row.append(self[i][j])
            new_vectors.append(Vector(row))
        return Matrix(new_vectors)
     
    def reduce(self: "Matrix", echelon=False, augmented=False, augment=None, factorize=False):

        # Perform a row reduction, possibly augmented, possibly to echelon form
        row_matrix = self.transpose()
        # Move all zero rows to bottom immediately
        for row_index in range(len(row_matrix)):
            if row_matrix[row_index].is_zero():
                for other_row_index in range(row_index + 1, len(row_matrix)):
                    if not row_matrix[other_row_index].is_zero():
                        row_matrix = row_matrix.swap(row_index, other_row_index)
                        break
                    
        if augmented:
            augmented_rows = augment.transpose()
            #Iterate over columns of row_matrix, finding the best pivot and swapping that row with the pivot row (pivot row = pivot column)
        for pivot_column in range(len(row_matrix[0])):
            # Skip zero rows (at the bottom)
            if row_matrix[pivot_column].is_zero():
                continue

            #If Echelon, Swap with first row that has first non-zero element in pivot column
            if echelon and row_matrix[pivot_column][pivot_column] == 0:
                for compare_row in range(pivot_column, len(row_matrix)):
                    if row_matrix[compare_row][pivot_column] != 0:
                        row_matrix = row_matrix.swap(pivot_column, compare_row)
                        if augmented:
                            augmented_rows = augmented_rows.swap(pivot_column, compare_row)
                        break

            # Swap the best pivot row with the pivot row (if not echelon)
            if not echelon:
                best_pivot_index = pivot_column
                for compare_row in range(pivot_column, len(row_matrix)):
                    if abs(row_matrix[compare_row][pivot_column]) > abs(row_matrix[best_pivot_index][pivot_column]):
                        best_pivot_index = compare_row
                row_matrix = row_matrix.swap(pivot_column, best_pivot_index)
                if augmented:   
                    augmented_rows = augmented_rows.swap(pivot_column, best_pivot_index)
            # Now we know that row_matrix[pivot_row][pivot_column] has the best pivot, so we can scale it to 1
            scale_factor = row_matrix[pivot_column][pivot_column]
            if scale_factor != 0 or scale_factor != 1:
                if not echelon:
                    row_matrix[pivot_column] = row_matrix[pivot_column].scale(1/scale_factor)
                    if augmented:
                        augmented_rows[pivot_column] = augmented_rows[pivot_column].scale(1/scale_factor)
            # Iterate over all remaining rows, reducing their values in row_matrix[remaining_row][pivot_column] to 0
            # If echelon is true, only reduce rows below the pivot row
            if echelon:
                start_row = pivot_column + 1
            else:
                start_row = 0
            for reduce_row in range(start_row, len(row_matrix)):
                if reduce_row == pivot_column:
                    continue
                if echelon:
                    scale_factor = row_matrix[reduce_row][pivot_column]/row_matrix[pivot_column][pivot_column]
                else:
                    scale_factor = row_matrix[reduce_row][pivot_column]
                row_matrix[reduce_row] = row_matrix[reduce_row] - row_matrix[pivot_column].scale(scale_factor)
                if augmented and factorize:
                    augmented_rows[reduce_row][pivot_column] = augmented_rows[reduce_row][pivot_column] + augmented_rows[pivot_column][pivot_column]*scale_factor
                elif augmented:
                    augmented_rows[reduce_row] = augmented_rows[reduce_row] - augmented_rows[pivot_column].scale(scale_factor)

        if augmented:
            return row_matrix.transpose(), augmented_rows.transpose()
        else:
            return row_matrix.transpose()
    
    def rank(self):
        #perform row reduction and then count the number of non-zero rows
        reduced_self_rows = self.reduce().transpose()
        rank = 0
        for i in range(len(reduced_self_rows)):
            if not reduced_self_rows[i].is_zero():
                rank += 1
        return rank
    
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
    
    def inverse(self):
        if len(self) != len(self[0]):
            raise ValueError("Matrix must be square to have an inverse")
        identity_matrix = Matrix.identity(len(self))
        reduced_self, inverse = self.reduce(augmented=True, augment=identity_matrix)
        return inverse
        
    def LU(self):
        if len(self) != len(self[0]):
            raise ValueError("Matrix must be square to have an inverse")
        identity_matrix = Matrix.identity(len(self))
        reduced_self, inverse = self.reduce(echelon=True, augmented=True, augment=identity_matrix, factorize=True)
        return inverse, reduced_self

    @classmethod
    def identity(cls, size):
        if size < 1:
            raise ValueError("Matrix must have at least one column")
        columns = []
        for i in range(size):
            vector = [0 for j in range(size)]
            vector[i] = 1
            columns.append(Vector(vector))
        return cls(columns)

def vector_matrix(vector):
    return Matrix([vector])

def vector_transpose(vector):
    return Matrix([Vector([i]) for i in vector])
