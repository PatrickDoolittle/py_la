from Vector import Vector

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
    if dp == 0:
        return True 
    else:
        return False