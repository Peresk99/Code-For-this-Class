Filename = input("Enter input file name: ")
print('\n%-15s%-10s%-10s' % ('Name' , 'Hours', 'Total Pay'))
for line in open(Filename):
    line = line.strip()
    
    if line != '':
        (nm, wage, hours) = line.split()

        wage = float(wage)
        hours = int(hours)
        pay = wage * hours

print('\n%-15s%-10s%-10s' % (nm, hours, pay))
