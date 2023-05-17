from Vector import *
from Matrix import *

#Vector projection test
v1 = Vector([3,1])
v2 = Vector([2,2])
v3 = vectorProjection(v1, v2)
v4 = vectorProjection(v2, v1)

#print(v3)
#print(v4)

# Linear Transformation for a latex document I'm working on
#LinearTransformation = Matrix([Vector([1,3]), Vector([-2,2])])
#Unit_square_vector = Vector([1,1])
#
#green_vector = Vector([1,2])
#green_vector_transformed = LinearTransformation * green_vector 
#print(green_vector_transformed)

# Matrix Inverse text
#A = Matrix([Vector([1,2]), Vector([2,3])])
#B = Matrix.identity(2)
#print(A)
#print(B)
#A_r, B_r = Matrix.row_reduce_augmented(A, B)
#print(A_r)
#print(B_r)

m_1 = Matrix([Vector([1,0,3]), Vector([2,1,8]), Vector([3,2,9])])
print(m_1)
m_2 = m_1.inverse()
print(m_2)

from Vector import *
from Matrix import *


''' 
Testground for refactoring row reduction functions

'''

def reduce(self: "Matrix", echelon=False, augmented=False, augment=None):

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
    for pivot_column in range(len(row_matrix)):
        # Skip zero rows (at the bottom)
        if row_matrix[pivot_column].is_zero():
            continue
        best_pivot_index = 0
        for compare_row in range(len(row_matrix)):
            if abs(row_matrix[compare_row][pivot_column]) > abs(row_matrix[best_pivot_index][pivot_column]):
                best_pivot_index = compare_row
        row_matrix = row_matrix.swap(pivot_column, best_pivot_index)
        if augmented:   
            augmented_rows = augmented_rows.swap(pivot_column, best_pivot_index)
        # Now we know that row_matrix[pivot_row][pivot_column] has the best pivot, so we can scale it to 1
        scale_factor = row_matrix[pivot_column][pivot_column]
        row_matrix[pivot_column] = row_matrix[pivot_column].scale(1/scale_factor)
        if augmented:
            augmented_rows[pivot_column] = augmented_rows[pivot_column].scale(1/scale_factor)
        # Iterate over all remaining rows, reducing their values in row_matrix[remaining_row][pivot_column] to 0
        # If echelon is true, only reduce rows below the pivot row
        if echelon:
            start_row = pivot_column + 1
        else:
            start_row = 0
        for remaining_row in range(start_row, len(row_matrix)):
            scale_factor = row_matrix[remaining_row][pivot_column]
            row_matrix[remaining_row] = row_matrix[remaining_row] - row_matrix[pivot_column].scale(scale_factor)
            if augmented:
                augmented_rows[remaining_row] = augmented_rows[remaining_row] - augmented_rows[pivot_column].scale(scale_factor)

    if augmented:
        return row_matrix.transpose(), augmented_rows.transpose()
    else:
        return row_matrix.transpose()


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
            #Find first non-zero element in column i, then swap that with row i
            for j in range(i+1, len(row_self[0])):
                if row_self[j][i] != 0:
                    row_self = row_self.swap(i, j)
                    break
            # Now we know that row i has a non-zero element in column i, divide X^T[i] by that element
            if row_self[i][i] != 0:
                row_self[i] = row_self[i].scale(1/row_self[i][i])
            # Iterate over all rows except row i
            for k in range(0, len(row_self)):
                if k == i:
                    continue
                row_self[k] = row_self[k] - row_self[i].scale(row_self[k][i])
        return row_self.transpose()
    
    def row_reduce_augmented(self, augment:"Matrix"):
        if not isinstance(augment, Matrix):
            raise TypeError("Augmented matrix must be a matrix")
        if len(self[0]) != len(augment[0]):
            raise ValueError("Matrices must have the same number of rows")
        self_rows = self.transpose()
        augmented_rows = augment.transpose()
        # Only row reduce with respect to the len(self) columns of the big matrix
        for i in range(len(self_rows)):
            #if row[i] is all zeros, skip it
            if self_rows[i].is_zero():
                continue

            #Find first non-zero element in column i of self_rows, then swap that row in both matrices
            for j in range(i+1, len(self_rows)):
                if self_rows[j][i] != 0:
                    self_rows = self_rows.swap(i, j)
                    augmented_rows = augmented_rows.swap(i, j)
                    break

            # Now we know that row i has a non-zero element in column i, divide that row in both matrices by that element
            scale_factor = self_rows[i][i]
            if scale_factor != 0:
                augmented_rows[i] = augmented_rows[i].scale(1/scale_factor)      
                self_rows[i] = self_rows[i].scale(1/scale_factor)



            # Iterate over all rows except row i
            for k in range(0, len(self_rows)):
                if k == i:
                    continue
                scale_factor = self_rows[k][i]
                self_rows[k] = self_rows[k] - self_rows[i].scale(scale_factor)
                augmented_rows[k] = augmented_rows[k] - augmented_rows[i].scale(scale_factor)
        return self_rows.transpose(), augmented_rows.transpose()
    