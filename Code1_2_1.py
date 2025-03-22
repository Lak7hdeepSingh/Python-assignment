v, t1 = map(float, input("v t: ").split())

# calculate the displacement
d = v * t1

v1, v2, t2 = map(float, input("v1 v2 t: ").split())

# calculate the acceleration
a = (v2 - v1) / t2

# print displacement
print(f"displacement: {d:.2f}")

# print acceleration
print(f"acceleration: {a:.2f}")
