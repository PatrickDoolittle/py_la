from typing import List
import math

class Vector:
    def __init__(self, elements: List[int]):
        if not isinstance(elements, list):
            raise TypeError("elements must be a list")
        if not all(isinstance(x,int) for x in elements):
            raise TypeError("elements must be a list of integers")
        self.elements = elements
        
    def __len__(self):
        return len(self.elements)
    
    def __str__(self):
        mod = self.modulus()
        return 'Vector: ' + str(self.elements) +  ' Modulus: ' + str(mod)
    
    def scale(self, scalar):
        product = self.elements
        for i in range(0,len(product)):
            product[i] = product[i] * scalar
        return Vector(product)
            
    def add(self, operand: Vector):
        if not isinstance(operand, 'Vector'):
            raise TypeError("operand is not a vector")
            
        
        
        if len(self) > len(operand):
            summand = self.elements
            for i in range (0,len(operand)):
                summand[i] += operand.elements[i]
            return Vector(summand)
        else: 
            summand = operand.elements
            for i in range (0, len(self)):
                summand[i] += self.elements[i]
            return Vector(summand)
        
    def modulus(self):
        mod = 0
        for i in range(0,len(self)):
            mod += self.elements[i]**2
        return math.sqrt(mod)
