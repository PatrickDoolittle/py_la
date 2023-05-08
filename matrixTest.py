'''
Unit Test for checking the Matrix Module Functionality
'''
from Matrix import *
from Vector import *

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

# Matrix Gram-Schmidt test
print("Matrix Gram-Schmidt test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_2 = m_1.gramSchmidt()
    assert m_2 == Matrix([Vector([1/math.sqrt(14), 2/math.sqrt(14), 3/math.sqrt(14)]), Vector([2/math.sqrt(21), 1/math.sqrt(21), 0]), Vector([1/math.sqrt(126), -10/math.sqrt(126), 5/math.sqrt(126)])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix Gram-Schmidt failed.  Check your code.")