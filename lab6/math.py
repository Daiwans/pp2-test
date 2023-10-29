import math

# Convert degrees to radians
degree = float(input("Input angle in degrees: "))
radian = math.radians(degree)
print(f"Angle in radians: {radian:.6f}")

# Calculate the area of a trapezoid
height = float(input("Input the height: "))
base1 = float(input("Input the length of the first base: "))
base2 = float(input("Input the length of the second base: "))
area = ((base1 + base2) / 2) * height
print(f"Area of the trapezoid: {area:.2f}")

# Calculate the area of a polygon
num_sides = int(input("Input number of sides: "))
length_side = float(input("Input the length of a side: "))
area = (num_sides * length_side ** 2) / (4 * math.tan(math.pi / num_sides))
print(f"Area of the polygon: {area:.2f}")

# Calculate the area of a parallelogram
base = float(input("Input the length of the base: "))
height = float(input("Input the height of the parallelogram: "))
area = base * height
print(f"Area of the parallelogram: {area:.1f}")

