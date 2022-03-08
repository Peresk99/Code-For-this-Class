filename = input("\nEnter a file name: ")
with open(filename, 'r') as file:
    Content = []

    for line in file:
        Content.append(line.strip())
        print("There are", len(Content), "lines in this file")

    while True:
        Linenum = int(input("Line Number: "))
        
        if Linenum <= 0:
            break

        else:
            print(data[Linenum - 1])
