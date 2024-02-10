def is_right_triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if is_right_triangle(side1, side2, side3):
    print("It's a right triangle.")
else:
    print("It's not a right triangle.")