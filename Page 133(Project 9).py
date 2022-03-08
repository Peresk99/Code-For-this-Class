Inputfile = input("Enter input filename: ")
Outputfile = input("Enter output filename: ")
with open(Inputfile, 'r') as f, open(Outputfile, 'w') as w:
    number = 0
    for line in f:
        number += 1
        w.write('{:>4}> {}'.format(number, line))
