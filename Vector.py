'''
Vector Object, 
elements are a list of floats
can be added 'w = u + v'
and indexed v[0] = v_x 

'''

from typing import List
import math


class Vector:
    def __init__(self, elements: List[float]):
        if not isinstance(elements, list):
            raise TypeError("elements must be a list")
        try:
            self.elements = [float(x) for x in elements]
        except TypeError as e:
            raise TypeError("Elements of list must be numerical")
        
    def __len__(self):
        return len(self.elements)
    
    def __add__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")
        summand = [self[i] + operand[i] for i in range(len(self))]
        return Vector(summand)

    def __mul__(self, operand):
        # I need to rewrite this method such that if a vector is multiplied by a matrix, the linear transformation occurs.
        if isinstance(operand, float) or isinstance(operand, int):
            return self.scale(operand)
        elif isinstance(operand, Vector):
            raise TypeError("Vector multiplication is not defined.")

    def __str__(self):
        mod = self.modulus()
        return str(self.elements)

    def __getitem__(self, index):
        return self.elements[index]
    
    def scale(self, scalar):
        try:
            data = [x * scalar for x in self.elements]
        except ValueError:
            raise ValueError("Scalar must be a numerical value")
        return Vector(data)

    def unitize(self):
        #Returns a unit vector in the direction of the vector
        # u = v/|v|
        new_vector = self.scale(1/self.modulus())
        return new_vector        
        

    def modulus(self):
        mod = 0
        for i in range(0,len(self)):
            mod += self[i]**2
        return math.sqrt(mod)




