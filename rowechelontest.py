from Matrix import *

# Transforms a matrix into row echelon form
def row_echelon(self):
    #Return transpose of self
    row_self = self.transpose()



#Quickly test the row_echelon function

# Create a matrix
vectors = [Vector([1, 2, 3]), Vector([4, 5, 6]), Vector([7, 8, 9])]
matrix = Matrix(vectors)
print("Original Matrix:")
print(matrix)
print("Row Echelon Form:")
print(matrix.row_echelon())