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