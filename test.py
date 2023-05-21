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
        for pivot_column in range(len(row_matrix)):
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