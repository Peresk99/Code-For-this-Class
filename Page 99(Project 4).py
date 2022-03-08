Height = float(input("Enter the height of the dropped ball: "))
Bounce = float(input("Enter the bounciness index index of the ball: "))
numberofbounces = int(input("Enter the number of times the ball can continue bouncing: "))
Distance = 0
Distance = Distance + Height
Height = Height * Bounce
Distance = Distance + Height
numberofbounces = 1
print("Total distance traveled is:", Distance)
