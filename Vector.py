from typing import List
import math

class Vector:
    def __init__(self, elements: List[float]):
        if not isinstance(elements, list):
            raise TypeError("elements must be a list")
        try:
            self.elements = [float(x) for x in elements]
        except ValueError as e:
            raise ValueError("Elements of list must be numerical")
        
    def __len__(self):
        return len(self.elements)
    
    def __add__(self, operand:"Vector"):
        if not isinstance(other, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")
        summand = [self[i] + operand[i] for i in range(len(self))]
        return Vector(summand)


    def __str__(self):
        mod = self.modulus()
        return 'Vector: ' + str(self.elements) +  ' Modulus: ' + str(mod)

    def __getitem__(self, index):
        return self.elements[index]
    
    def scale(self, scalar):
        product = self.elements
        for i in range(0,len(product)):
            product[i] = product[i] * scalar
            
    def modulus(self):
        mod = 0
        for i in range(0,len(self)):
            mod += self[i]**2
        return math.sqrt(mod)




