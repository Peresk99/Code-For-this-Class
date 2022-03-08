count = 0
s = 0
num = int(input("Enter a number: "))
while (num != ""):
       s += float(num)
       count += 1
       num = input("Enter a number: ")
print("Sum: " + str(s))
print("Average: " + str(s / count))
