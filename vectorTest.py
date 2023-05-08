'''
Unit test for checking the Vector Module Functionality
'''

from Vector import *

# Vector creation test
print("Vector creation test and to-string test.")
try: 
    v_1 = Vector([1,2,3])
except Exception:
    print("Vector creation failed.  Check your code.")
print("Passed")

# Vector length test
print("Vector length test.")
try:
    assert len(v_1) == 3
    print("Passed")
except AssertionError:
    print("Vector length failed.  Check your code.")

# Vector equality test
v_2 = Vector([1,2,3])
print("Vector equality test.")
try:
    assert v_1 == v_2
    print("Passed")
except AssertionError:
    print("Vector equality failed.  Check your code.")

# Vector addition test
print("Vector addition test.")
try:
    v_3 = v_1 + v_2
    assert v_3 == Vector([2,4,6])
    print("Passed")
except AssertionError:
    print("Vector addition failed.  Check your code.")
    
# Vector Scaling test
print("Vector scaling test.")
try:
    v_1prime = v_1.scale(5)
    assert v_1prime == Vector([5,10,15])
    print("Passed")
except AssertionError:
    print("Vector scaling failed.  Check your code.")

# Vector dot product test

# Vector modulus test

# Vector unitize test

# Vector projection test

## Vector equality test


