from Vector import *
''' This is a unit test to verify that the Vector module is working correctly.

Vector methods:
__init__: takes a list of numerical values and stores as floats
__len__: Allows the built in len(object) function to return the size of the vector by checking the size of the vector's list
__str__: Turns the vector into a string giving all relavant information in a readable format
__getitem__: Allows indexing directly into the elements of the Vector object by indexing the object itself (Vector[i] not Vector.elements[i])
__add__: Allows you to add two vectors by using the '+' symbol: "v3 = v1 + v2" sets v3 to a vector that is the sum of v1 and v2.
scale: Takes a numerical value and multiplies each component of the vector by this value (maybe make an inverse flag?)
modulus: Finds the size of the vector by taking the square root of the sum of the squares of the components.

''' 

#init test
print("init test")
print("Testing for list format.")
try: 
    v = Vector(5)
except TypeError as e:
    print("pass")
except Exception as e:
    print("fail")

print("Checking elements are numerical.")

try:
    v = Vector(['a','b','c'])
except ValueError as e:
    print("Pass")
except Exception as e:
    print("Fail")

#str test
v_1 = Vector([1,2,3])
print("Testing Vector readout.")
print(str(v_1))

#add test
print("Vector addition test, should be [1,1,1] + [1,2,3] = [2,3,4].")
v_2 = Vector([1,1,1])
v_3 = v_1 + v_2
print(str(v_3))

#__getitem__ test
print("Index test: should be 4.")
print(v_3[2])

# scale test
print("Scale test, should be [4,6,8].")
v_3 = v_3.scale(2)
print(str(v_3))

# Unitize test
print("Unitize test, should be [.37,.55,.74].")
print(str(v_3))
print(str(v_3.modulus()))
v_3 = v_3.unitize()
print(str(v_3))
print(str(v_3.modulus()))

#Unitise three more vectors
print("Unitize three more vectors.")
v_4 = Vector([1,2,3])
v_5 = Vector([4,5,6])
v_6 = Vector([7,8,9])
v_4 = v_4.unitize()
v_5 = v_5.unitize()
v_6 = v_6.unitize()
print(str(v_4))
print(str(v_5))
print(str(v_6))
print(str(v_4.modulus()))
print(str(v_5.modulus()))
print(str(v_6.modulus()))

'''
Unit Test of the suite of functions for vector operations VectorOperations.py

Vector functions:
dot(v,u): Returns the dot product of two vectors
cross(v,u): Returns the cross product of two vectors in 3d space. Order matters (cross(v,u) != cross(u,v))
scalarProjection(v,u): Returns the scalar projection of vector v onto u. 
vectorProjection(v,u): Returns a vector in with the magnitude and direction of the projection of v onto u.
orthogonal(v,u): Checks if two vectors are orthogonal (their dot product is zero)...

'''

print("Dot Product Test, should be [1,2,3] * [1,1,1] = 6.")
v = Vector([1,2,3])
u = Vector([1,1,1])
print(dot(u,v))


print("Cross Product Test: should be [-1,2,-1].")
print(cross(v,u))
print("Scalar Projection Test: should be 3.46.")
print(f" {scalarProjection(v,u):.2f}")
print("Vector Projection Test: should be [2,2,2].")
w = vectorProjection(v,u)
print(str(w))
print("Orthogonality check test, should be False and then True.")
print(orthogonal(u,v))
v = Vector([5,1,0])
u = Vector([1,-5,0])
print(orthogonal(v,u))


