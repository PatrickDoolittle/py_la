'''
Vector Object, 
elements are a list of floats
'''


from typing import List
import math


class Vector:
    def __init__(self, elements: List[float]):
        if not isinstance(elements, list):
            raise TypeError("elements must be a list")
        if len(elements) == 0:
            raise ValueError("Vector must have at least one element")
        try:
            self.elements = [float(x) for x in elements]
        except TypeError as e:
            raise TypeError("Elements of list must be numerical")
        except Exception as e:
            raise Exception("Fail!")
        
    def __len__(self):
        return len(self.elements)
    
    def __eq__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if all([abs(self[i] - operand[i]) < .0001 for i in range(len(self))]):
            return True
        else:
            return False
    
    def __add__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")
        summand = [self[i] + operand[i] for i in range(len(self))]
        return Vector(summand)
    
    def __sub__(self, operand:"Vector"):
        if not isinstance(operand, Vector):
            raise TypeError("Operand is not a vector.")
        if len(self) != len(operand):
            raise ValueError("Vectors of mismatched size")
        difference = [self[i] - operand[i] for i in range(len(self))]
        return Vector(difference)

    def __mul__(self, operand):
        if isinstance(operand, float) or isinstance(operand, int):
            return self.scale(operand)
        elif isinstance(operand, Vector):
            raise TypeError("Vector multiplication is not defined.")

    def __str__(self):
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

'''
Related functions not made methods
'''
def dot(a:'Vector', b: 'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size.")
    sum = 0
    for i in range(0,len(a)):
        sum += (a[i] * b[i])
    return sum

def cross(a:'Vector', b: 'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if not len(b) <= 3 and len(a) <= 3:
        raise ValueError("Vectors need be size 3 or less")
    if not len(b) > 1 and len(a) > 1 :
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
    projection_elements = b.elements.copy()
    projection = Vector(projection_elements)
    projection = projection.scale(scaling_factor)
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

