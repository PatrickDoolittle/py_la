from Vector import Vector as Vector

v_1 = Vector([1.0,2.0,3.0])
v_2 = Vector([1,1,1])

v_6 = v_1.vectorProjection(v_2)
print(v_1.dot(v_2))
print(v_2.modulus())
print(v_1.scalarProjection(v_2))
print(str(v_2.scale(1 / v_2.modulus())))
print(str(v_6))
