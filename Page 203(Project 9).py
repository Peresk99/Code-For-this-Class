Filename = input("Enter the file name: ")
total = 0; count = 0
fopen = open(Filename, 'r')
content = fopen.read().split()
for line in content:
    sum += int(line)
    count += 1
f.open.close()
Average = float(sum)/count
print("The average is: ", Average)
