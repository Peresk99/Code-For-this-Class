SideA = float(input("Enter the first side: "))
SideB = float(input("Enter the second side: "))
SideC = float(input("Enter the third side: "))
if ((SideA * 2 == SideB * 2 + SideC * 2) or (SideA * 2 + SideB * 2 == SideC * 2) or (SideA * 2 + SideC * 2 == SideB * 2)):
    print("The triangle is a right triangle")
else:
    print("The triangle is not a right triangle")
