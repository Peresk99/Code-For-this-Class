Message = input("Enter a message: ")
Distancevalue = int(input("Enter a distance value: "))
Endresult = ""
for x in Message:
    Endresult += chr(ord(x) + Distancevalue)
print("" + Endresult)
