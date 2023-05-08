'''
Unit test for checking the Vector Module Functionality
'''

from Vector import *

# Vector creation test
print("Vector creation test and to-string test.")
try: 
    v_1 = Vector([1,2,3])
except Exception:
    raise Exception("Vector creation failed.  Check your code.")
print("Passed")

# Checking vector of empty list fails
print("Vector creation test with empty list.")
try:
    v_1 = Vector([])
    raise Exception("Vector creation failed.  Check your code.")
except ValueError:
    print("Passed")
except Exception:
    raise Exception("Vector creation failed.  Check your code.")

# Vector length test
print("Vector length test.")
try:
    assert len(v_1) == 3
    print("Passed")
except AssertionError:
    raise Exception("Vector length failed.  Check your code.")

# Vector equality test
v_2 = Vector([1,2,3])
print("Vector equality test.")
try:
    assert v_1 == v_2
    print("Passed")
except AssertionError:
    raise Exception("Vector equality failed.  Check your code.")

# Vector item assignment test
print("Vector item assignment test.")
try:
    v_1[0] = 5
    assert v_1 == Vector([5,2,3])
    print("Passed")
except AssertionError:
    raise Exception("Vector item assignment failed.  Check your code.")

v_1 = Vector([1,2,3])

# Vector addition test
print("Vector addition test.")
try:
    v_3 = v_1 + v_2
    assert v_3 == Vector([2,4,6])
    print("Passed")
except AssertionError:
    raise Exception("Vector addition failed.  Check your code.")
    
# Vector Scaling test
print("Vector scaling test.")
try:
    v_1prime = v_1.scale(5)
    assert v_1prime == Vector([5,10,15])
    print("Passed")
except AssertionError:
    raise Exception("Vector scaling failed.  Check your code.")

# Vector dot product test
print("Vector dot product test.")
try:
    assert dot(v_1, v_2) == 14
    print("Passed")
except AssertionError:
    raise Exception("Vector dot product failed.  Check your code.")

# Vector modulus test
print("Vector modulus test.")
try:
    assert v_1.modulus() == math.sqrt(14)
    print("Passed")
except AssertionError:
    raise Exception("Vector modulus failed.  Check your code.")


# Vector unitize test
print("Vector unitize test.")
try:
    v_1prime = v_1.unitize()
    assert v_1prime == Vector([1/math.sqrt(14),2/math.sqrt(14),3/math.sqrt(14)])
    print("Passed")
except AssertionError:
    raise Exception("Vector unitize failed.  Check your code.")


# Vector projection test
print("Vector projection test.")
try:
    v_1prime = Vector([1,2,3])
    v_2prime = Vector([1,1,1])
    v_3prime = vectorProjection(v_1prime, v_2prime)
    assert v_3prime == Vector([2,2,2])
    print("Passed")
except AssertionError:
    raise Exception("Vector projection failed.  Check your code.")


# Vector orthogonality test 
print("Vector orthogonality rejection test.")
try:
    v_1prime = Vector([1,2,3])
    v_2prime = Vector([1,1,1])
    assert orthogonal(v_1prime, v_2prime) == False
    print("Passed")
except AssertionError:
    raise Exception("Vector orthogonality failed.  Check your code.")


print("Vector orthonganality confirmation test.")
try:
    v_1prime = Vector([1,2,3])
    v_2prime = Vector([2,-1,0])
    assert orthogonal(v_1prime, v_2prime) == True
except AssertionError:
    raise Exception("Vector orthogonality failed.  Check your code.")



