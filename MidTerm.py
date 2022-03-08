#Peremobowei Kereotubo
#Spring 2022
#Michael Schnell

Name = input("Enter a filename: ")
Output = input("Enter an output file: ")

with open("MidTermExamLabTestFile.txt", 'r') as file:
    contents = []
    count = 0

    for line in file:
        contents.append(line.strip())
        print("")


    for key in list(d.keys()):
        print(key, ":", d[key])
        
