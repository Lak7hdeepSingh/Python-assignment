# Read inputs for force calculation
m, a = map(float, input() .split())

# calculate the force
f = m*a

# Read inputs for shear stress calculation
F, A = map(float, input().split())

# calculate the Shear stress
t = F/A

# print the force

print("Force:",f)
# print the Shear stress
print(f"Shear stress: {t :. 2f}")