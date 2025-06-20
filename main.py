from vector3d import Vector3D

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 2  =", v1 * 2)
print("Dot product =", v1.dot(v2))
print("Cross product =", v1.cross(v2))
print("Are they equal?", v1 == v2)