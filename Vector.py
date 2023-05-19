'''
Vector Object, 
elements are a list of floats
'''


from typing import List
import math


class Vector:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError("elements must be a list")
        if len(elements) == 0:
            raise ValueError("Vector must have at least one element")
        try:
            self.elements = [float(x) for x in elements]
        except TypeError as e:
            raise TypeError("Elements of list must be numerical")
        except Exception as e:
            raise Exception("Vector init error")
        
    def __len__(self):
        return len(self.elements)
    
    def __eq__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        return all([abs(self[i] - operand[i]) < .0001 for i in range(len(self))])
    
    def __add__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand in vector addition is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")
        summand = [self[i] + operand[i] for i in range(len(self))]
        return Vector(summand)
    
    def __sub__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand in vector addition is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")
        difference = [self[i] - operand[i] for i in range(len(self))]
        return Vector(difference)

    def __mul__(self, operand):
        if isinstance(operand, float) or isinstance(operand, int):
            return self.scale(operand)
        elif isinstance(operand, Vector):
            raise TypeError("Vector-vector multiplication is not defined.")

    def __str__(self):
        return str(self.elements)

    def __getitem__(self, index):
        return self.elements[index]
    
    def __setitem__(self,index, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Value must be a number")
        self.elements[index] = value

    def is_zero(self):
        for i in range(len(self)):
            if self[i] > 0.00001 or self[i] < -0.00001:
                return False
        return True
    
    def scale(self, scalar):
        if self.is_zero():
            return Vector(self.elements)
        if not isinstance(scalar, float) and not isinstance(scalar, int):
            raise TypeError("Scalar must be a number")
        data = [ x * scalar for x in self.elements]
        return Vector(data)

    def unitize(self):
        if self.is_zero():
            raise Exception("Cannot unitize a zero vector")
        new_vector = self.scale(1/self.modulus())
        return new_vector        

    def modulus(self):
        if self.is_zero():
            return 0
        mod = 0
        for i in range(0,len(self)):
            mod += self[i]**2
        return math.sqrt(mod)
    
    @classmethod
    def zero(cls, size):
        if size < 1:
            raise ValueError("Vector must have at least one element")
        data = [0 for i in range(size)]
        return cls(data)


'''
Related functions not made methods
'''
def dot(a:'Vector', b: 'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Dot product is only defined between vectors.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size.")
    sum = 0
    for i in range(0,len(a)):
        sum += (a[i] * b[i])
    return sum

def cross(a:'Vector', b: 'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if not len(b) <= 3 or len(a) <= 3:
        raise ValueError("Vectors need be size 3 or less")
    if not len(b) > 1 or len(a) > 1 :
        raise ValueError("Vectors need to be greater than size 1")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")
    if len(a) == 2:
        new_data = [0,0,  a[0] * b[1] - a[1] * b[0]]
        return Vector(new_data)
    else:
        new_data = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0] ]
        return Vector(new_data)
    
def scalarProjection(a:'Vector', b:'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")
    return dot(a,b)/ b.modulus() 

def vectorProjection(a:'Vector', b:'Vector'): 
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")
    scaling_factor = dot(a,b) / b.modulus()**2
    projection = b.scale(scaling_factor)
    return projection

def orthogonal(a:'Vector', b:'Vector'):
    if not isinstance(a, Vector) or not isinstance(b,Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")

    dp = dot(a,b)
    if dp < 0.00001 and dp > -0.00001:
        return True 
    else:
        return False

