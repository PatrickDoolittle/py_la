from Vector import Vector
from VectorOperations import *
'''
Unit Test of the suite of functions for vector operations VectorOperations.py

Vector functions:
dot(v,u): Returns the dot product of two vectors
cross(v,u): Returns the cross product of two vectors in 3d space. Order matters (cross(v,u) != cross(u,v))
scalarProjection(v,u): Returns the scalar projection of vector v onto u. 
vectorProjection(v,u): Returns a vector in with the magnitude and direction of the projection of v onto u.
orthogonal(v,u): Checks if two vectors are orthogonal (their dot product is zero)...

'''

print("Dot Product Test, should be [1,2,3] * [1,1,1] = 6")
v = Vector([1,2,3])
u = Vector([1,1,1])
print(dot(u,v))

