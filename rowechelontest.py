from Matrix import *

# Transforms a matrix into row echelon form
def row_echelon(Matrix):
    #Return transpose of self
    row_self = Matrix.transpose()
    for i in range(len(row_self)):
        #Find first non-zero element in self[i]
        for j in range(len(row_self[0])):
            if row_self[i][j] != 0:
                row_self = row_self.swap(i, j)
                break
        # Now we know that row i has a non-zero element in column i, divide X^T[i] by that element
        row_self[i] = row_self[i].scale(1/row_self[i][i])
        print(row_self.transpose())

        # Iterate over remaining rows reducing them in column i
        for k in range(i+1, len(row_self)):
            row_self[k] = row_self[k] - row_self[i].scale(row_self[k][i])
        return row_self.transpose()




#Quickly test the row_echelon function

# Create a matrix
vectors = [Vector([1, 2, 3]), Vector([4, 5, 6]), Vector([7, 8, 9])]
matrix = Matrix(vectors)
print("Original Matrix:")
print(matrix)
print("Row Echelon Form:")
print(row_echelon(matrix))