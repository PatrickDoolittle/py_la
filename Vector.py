from typing import List
import math

class Vector:
    def __init__(self, elements: List[float]):
        if not isinstance(elements, list):
            raise TypeError("elements must be a list")
        self.elements = [float(x) for x in elements]
        
    def __len__(self):
        return len(self.elements)
    
    def __str__(self):
        mod = self.modulus()
        return 'Vector: ' + str(self.elements) +  ' Modulus: ' + str(mod)

    def __getitem__(self, index):
        return self.elements[index]
    
    def scale(self, scalar):
        product = self.elements.copy()
        for i in range(0,len(product)):
            product[i] = product[i] * scalar
        return Vector(product)
            
    def modulus(self):
        mod = 0
        for i in range(0,len(self)):
            mod += self[i]**2
        return math.sqrt(mod)

    def add(self, operand: 'Vector'):
        if not isinstance(operand, Vector):
            raise TypeError("operand is not a vector")
              
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")

        summand = self.elements.copy()
        for i in range(0, len(self)):
            summand[i] += operand[i]
        return Vector(summand)
        
    def dot(self, operand: 'Vector'):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size.")
        sum = 0
        for i in range(0,len(self)):
            sum += (self[i] * operand[i])
            #print(str(self[i]) + ' * ' + str(operand[i]) + ' = ' + str(sum) )
        return sum

    def cross(self, operand: 'Vector'):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if not len(operand) <= 3 & len(self) <= 3:
            raise IndexError("Vectors need be size 3 or less")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")

        if len(self) == 2:
            new_data = [0,0, (self[0] * operand[1] - self[1] * operand[0])]
            return Vector(new_data)
        else:
            new_data = [(self[1] * operand[2] - self[2] * operand[1]), (self[2] * operand[0] - self[0] * operand[1]), (self[0] * operand[1] - self[1] * operand[0]) ]
            return Vector(new_data)

    def orthogonal(self, operand:'Vector'):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")

        dp = self.dot(operand)
        if dp == 0:
            return True 
        else:
            return False

    def scalarProjection(self, operand:'Vector'):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")

        return self.dot(operand) / operand.modulus()   

    def vectorProjection(self, operand:'Vector'): 
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")

        operand_hat = operand.scale(1 / operand.modulus() )
        return operand_hat.scale( self.scalarProjection(operand))
        
