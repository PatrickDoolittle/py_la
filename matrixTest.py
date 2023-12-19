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

try:
    v_1 = Vector([2,3.5])
    v_2 = Vector([-2,2])
    m_1 = Matrix([v_1, v_2])
    v_3 = Vector([1,1])
    v_4 = m_1 * v_3
    assert v_4 == Vector([0,5.5])
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

try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6])])
    m_2 = Matrix([Vector([1,2]), Vector([4,5]), Vector([7,8])])
    m_3 = m_1 @ m_2
    assert m_3 == Matrix([Vector([9,12,15]), Vector([24,33,42]), Vector([39,54,69])])
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

# Matrix Column swap test  
print("Matrix Column swap test.")
try:
    m_1 = Matrix([Vector([1,2,3]), Vector([4,5,6]), Vector([7,8,9])])
    m_2 = m_1.swap(0,1)
    assert m_2 == Matrix([Vector([4,5,6]), Vector([1,2,3]), Vector([7,8,9])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix column swap failed.  Check your code.")

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
    m_2 = m_1.reduce()
    assert m_2 == Matrix([Vector([1,-0,0]), Vector([0,1,0]), Vector([-1,2,0])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row reduction failed.  Check your code.")

try:
    m_1 = Matrix([Vector([1,0,3]), Vector([2,1,8]), Vector([3,2,9])])
    m_2 = m_1.reduce()
    assert m_2 == Matrix([Vector([1,0,0]), Vector([0,1,0]), Vector([0,0,1])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row reduction failed.  Check your code.")

try: 
    m_1 = Matrix([Vector([6,5,3]), Vector([12,14,8]), Vector([18,31,18])])
    m_2 = m_1.reduce()
    assert m_2 == Matrix([Vector([1,0,0]), Vector([0,1,0]), Vector([0,0,1])])
    print("Paseed")
except AssertionError:
    raise Exception("Matrix row reduction failed.  Check your code.")

# Matrix row echelon test
print("Matrix row echelon test.")
try:
    m_1 = Matrix([Vector([0,8,0]), Vector([0,9,17]), Vector([1,2,9])])
    m_2 = m_1.reduce(echelon=True)
    assert m_2 == Matrix([Vector([8,0,0]), Vector([9,17,0]), Vector([2,9,1])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row echelon failed.  Check your code.")

# Test row echelon with matrix that has zero rows at beginning
try:
    m_1 = Matrix([Vector([0,0,0]), Vector([0,9,17]), Vector([1,2,9])], transpose=True)
    m_2 = m_1.reduce(echelon=True)
    assert m_2.transpose() == Matrix([Vector([1,2,9]), Vector([0,9,17]), Vector([0,0,0])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row echelon failed.  Check your code.")

# Test row echelon with matrix that has every element filled
try:
    m_1 = Matrix([Vector([6,5,3]), Vector([12,14,8]), Vector([18,31,18])])
    m_2 = m_1.reduce(echelon=True)
    assert m_2 == Matrix([Vector([6,0,0]), Vector([12,4,0]), Vector([18,16,1])])
    print("Passed")
except AssertionError:
    raise Exception("Matrix row echelon failed.  Check your code.")

# Augmented Matrix row echelon test
print("Augmented Matrix row reduction test.")
try:
    m_1 = Matrix([Vector([1,0,3]), Vector([2,1,8]), Vector([3,2,9])])
    m_2 = Matrix([Vector([1,0,0]), Vector([0,1,0,]), Vector([0,0,1])])
    m_3, m_4 = m_1.reduce(augmented=True, augment=m_2)
    assert m_3 == Matrix([Vector([1,0,0]), Vector([0,1,0]), Vector([0,0,1])])
    assert m_4 == Matrix([Vector([7/4.,-3/2.,3/4.]), Vector([-3/2.,0.,1/2.]), Vector([-1/4.,1/2.,-1/4])])
    print("Passed")
except AssertionError:
    raise Exception("Augmented Matrix row reduction failed.  Check your code.")

# Lower Upper Decomposition test
print("Lower Upper Decomposition test.")
try:   
    m_1 = Matrix([Vector([1,4,3]), Vector([2,6,7]), Vector([3,9,1])])
    m_2, m_3 = m_1.LU()

    assert m_2 @ m_3 == m_1
    print("Passed")
except AssertionError:
    raise Exception("LU decomposition failed.  Check your code.")


# Variable Size Identity Matrix Test
print("Variable Size Identity Matrix Test")
try:
    m_1 = Matrix.identity(3)
    assert m_1 == Matrix([Vector([1,0,0]), Vector([0,1,0]), Vector([0,0,1])])
    print("Passed")
except AssertionError:
    raise Exception("Variable Size Identity Matrix Test failed.  Check your code.")

# Matrix __setitem__ test
print("Matrix Element Assigment test")
try:
    m_1 = Matrix.identity(3)
    m_1[0][0] = 5
    assert m_1 == Matrix([Vector([5,0,0]), Vector([0,1,0]), Vector([0,0,1])])
    print("Passed") 
except AssertionError:
    print("Element Assignment failed.  Check your code.")

print("Matrix Vector Assignment test")
try:
    m_1 = Matrix.identity(3)
    m_1[0] = Vector([5,5,5])
    assert m_1 == Matrix([Vector([5,5,5]), Vector([0,1,0]), Vector([0,0,1])])
    print("Passed")
except AssertionError:
    print("Vector Assignment failed.  Check your code.")


print("Printing string form of 3x3 Matrix")
try:
    m_1 = Matrix([Vector([1,4,7]), Vector([2,5,8]), Vector([3,6,9])])
    print(m_1)
except Exception:
    print("Printing failed.  Check your code.")

# Matrix Rank Test
print("Matrix Rank Test")
try:
    m_1 = Matrix([Vector([1,4,7]), Vector([2,5,8]), Vector([3,6,9])])
    assert m_1.rank() == 2
    print("Passed")
except AssertionError:
    raise Exception("Rank failed.  Check your code.")

# Vector Transpose Test
print("Vector Transpose Test")
try:
    v_1 = Vector([1,2,3])
    v_1T = vector_transpose(v_1)
    assert v_1T[0][0] == 1
    assert v_1T[1][0] == 2
    assert v_1T[2][0] == 3
    print("Passed")
except AssertionError:
    raise Exception("Vector Transpose failed.  Check your code.")


# Matrix Vector Test
print("Matrix Vector Test")
try:
    v_1 = Vector([1,2,3])
    v_1M = vector_matrix(v_1)
    print(v_1M)
    assert v_1M == Matrix([Vector([1,2,3])])
except AssertionError:
    raise Exception("Matrix Vector failed.  Check your code.")

# Null Basis Test
print("Nullspace Basis Test")
m_5 = Matrix([Vector([1,2,-1]),Vector([3,6,-3]),Vector([3,9,3]),Vector([2,7,4])])
print(m_5.nullbasis())
print(m_5.nullbasis1())


m_1 = Matrix([Vector([2,.5]),Vector([.5,2])])
print(str(m_1) + '\n')
vectors = [Vector([1,0]),Vector([0,1]),Vector([1,1]),Vector([1,-1]),Vector([2,1]),Vector([4,9])]
for v in vectors:
    print("Transforming " + str(v))
    print(m_1 * v)
    print()