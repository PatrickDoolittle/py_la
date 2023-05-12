from Vector import *
from Matrix import *
v1 = Vector([3,1])
v2 = Vector([2,2])
v3 = vectorProjection(v1, v2)
v4 = vectorProjection(v2, v1)

print(v3)
print(v4)