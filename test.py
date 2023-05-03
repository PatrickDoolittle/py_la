from Vector import Vector as Vector

v_1 = Vector([1,2,3])
v_2 = Vector([1,1,1])
v_2 = v_2.scale(2)
print(str(v_2))
v_3 = v_1.add(v_2)
print(str(v_3))
print(str(v_2))
print(v_3.dot(v_2))

v_4 = Vector([1,2,3,4])
v_5 = v_1.cross(v_2)
print(str(v_5))
print(v_1.orthogonal(v_2))
