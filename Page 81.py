number = int(input("Enter the numeric grade: "))
if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'
print("The letter grade is", letter)

number = int(input("Enter the numeric grade: "))
if number > 100:
    print("Error: grade must be between 100 and 0"))
elif number < 0:
    print("Error: grade must be between 100")
else:
