
def dot(a:'Vector', b: 'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size.")
    sum = 0
    for i in range(0,len(a)):
        sum  (a[i] * b[i])
    return sum

def cross(a:'Vector', b: 'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if not len(b) <= 3 & len(a) <= 3:
        raise IndexError("Vectors need be size 3 or less")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")
    if len(a) == 2:
        new_data = [0,0,  a[0] * b[1] - a[1] * b[0]]
        return Vector(new_data)
    else:
        new_data = [(a[1] * b[2] - a[2] * b[1]), (a[2] * b[0] - a[0] * b[1]), (a[0] * b[1] - a[1] * b[0]) ]
        return Vector(new_data)
    
def scalarProjection(a:'Vector', b:'Vector'):
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")
    return a.dot(b) / b.modulus()   

def vectorProjection(a:'Vector', b:'Vector'): 
    if not isinstance(b, Vector) or not isinstance(a, Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")
    b_hat = b.scale(1 / b.modulus() )
    return b_hat.scale( a.scalarProjection(b))
        
def orthogonal(a:'Vector', b:'Vector'):
    if not isinstance(a, Vector) or not isinstance(b,Vector):
        raise TypeError("Operand is not a vector.")
    if len(a) != len(b):
        raise ValueError("Vectors of mismatched size")

    dp = a.dot(b)
    if dp == 0:
        return True 
    else:
        return False