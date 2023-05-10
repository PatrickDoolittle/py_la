'''
Unit Test for checking the Matrix Module Functionality
'''
from Matrix import *
from Vector import *

print("Testing Matrix Module")

# Matrix creation test
print("Matrix creation test and to-string test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    print("Passed")
except Exception:
    raise Exception("Matrix creation failed.  Check your code.")

# Checking matrix of empty list fails
print("Matrix creation test with empty list.")
try:
    m_1 = Matrix([])
    raise Exception("Matrix creation failed.  Check your code.")
except ValueError:
    print("Passed")
except Exception:
    raise Exception("Matrix creation failed.  Check your code.")

# Matrix length test
print("Matrix length test.")
try:
    assert len(m_1) == 3
    print("Passed")
except AssertionError:
    raise Exception("Matrix length failed.  Check your code.")

# Matrix equality test
m_2 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
print("Matrix equality test.")
try:
    assert m_1 == m_2
    print("Passed")
except AssertionError:
    raise Exception("Matrix equality failed.  Check your code.")

# Matrix addition test
print("Matrix addition test.")
try:
    m_3 = m_1 + m_2
    assert m_3 == Matrix([Vector([2,4,6]), Vector([8,10,12]), Vector([14,16,18])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix addition failed.  Check your code.")

# Matrix subtraction test
print("Matrix subtraction test.")
try:
    m_3 = m_1 - m_2
    assert m_3 == Matrix([Vector([0,0,0]), Vector([0,0,0]), Vector([0,0,0])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix subtraction failed.  Check your code.")

# Matrix scaling test
print("Matrix scaling test.")
try:
    m_3 = m_1.scale(5)
    assert m_3 == Matrix([Vector([5,10,15]), Vector([20,25,30]), Vector([35,40,45])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix scaling failed.  Check your code.")

# Matrix-Vector multiplication test
print("Matrix-Vector multiplication test.")
try:
    v_1 = Vector([1,2,3])
    v_2 = Vector([4,5,6])
    v_3 = Vector([7,8,9])
    m_1 = Matrix([v_1, v_2, v_3])
    v_3 = m_1 * v_1
    assert v_3 == Vector([30,36,42])
    print("Passed")
except AssertionError:
    raise Exception("Matrix- Vector multiplication failed.  Check your code.")

# Matrix-Matrix multiplication test
print("Matrix-Matrix multiplication test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_2 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_3 = m_1 @ m_2
    assert m_3 == Matrix([Vector([30,36,42]), Vector([66,81,96]), Vector([102,126,150])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix-Matrix multiplication failed.  Check your code.")

# Matrix transpose test
print("Matrix transpose test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_2 = m_1.transpose()
    assert m_2 == Matrix([Vector([1,4,7]), Vector([2,5,8]), Vector([3,6,9])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix transpose failed.  Check your code.")

# Matrix row swap test  
print("Matrix row swap test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_2 = m_1.swap(0,1)
    assert m_2 == Matrix([Vector([4,5,6]), Vector([1,2,3]), Vector([7,8,9])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row swap failed.  Check your code.")

# Matrix element assignment test
print("Matrix element assignment test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_1[0][0] = 5
    assert m_1 == Matrix([Vector([5,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix element assignment failed.  Check your code.")

# Matrix Column Swap Test
print("Matrix column swap test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_2 = m_1.swap(0,1)
    assert m_2 == Matrix([Vector([4,5,6] ), Vector([1,2,3]), Vector([7,8,9])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix column swap failed.  Check your code.")

# Matrix row reduction test 
print("Matrix row reduction test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_2 = m_1.row_reduce()
    assert m_2 == Matrix([Vector([1,-0,0]), Vector([0,1,0]), Vector([-1,2,0])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row reduction failed.  Check your code.")

# Matrix row echelon test
print("Matrix row echelon test.")
try:
    m_1 = Matrix([Vector([0,8,0]), Vector([0,9,17]), Vector([1,2,9])])
    m_2 = m_1.row_echelon()
    assert m_2 == Matrix([Vector([8,0,0]), Vector([9,17,0]), Vector([2,9,1])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row echelon failed.  Check your code.")

print("All tests passed!")