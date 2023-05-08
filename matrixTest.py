'''
Unit Test for checking the Matrix Module Functionality
'''
from Matrix import *
from Vector import *

# Matrix creation test
print("\n \nMatrix creation test and to-string test.")
m_1 = Matrix([Vector([1,2,3]),Vector([4,5,6]),Vector([7,8,9])])
print(str(m_1))

# Matrix length test
print("\n \nMatrix column length test.")
print(str(len(m_1)))

#Matrix addition test
print("\n \nMatrix addition test.")
m_2 = Matrix([Vector([1,2,3]),Vector([4,5,6]),Vector([7,8,9])])
m_3 = m_1 + m_2
print(str(m_3))


# Matrix Column Index test 
print("\n \nMatrix column index test.")
print(str(m_1[0]))

# Matrix element index test
print("\n \nMatrix element index test.")
print(str(m_1[0][0]))

# Matrix-Matrix multiplication test
print("\n \nMatrix-Matrix multiplication test.")
m_2 = Matrix([Vector([1,2,3]),Vector([4,5,6]),Vector([7,8,9])])
m_3 = m_1 @ m_2
print(str(m_3))



# Matrix-Vector multiplication test
print("\n \nMatrix-Vector multiplication test.")
v_1 = Vector([1,2,3])
v_2 = m_1 * v_1
print(str(v_2))


# Matrix transpose test
print("\n \nMatrix transpose test.")
m_2 = m_1.transpose()
print(str(m_2))
