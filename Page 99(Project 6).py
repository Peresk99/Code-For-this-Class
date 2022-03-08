SumApprox = 0

float(SumApprox)

Denominator = 1

int(Denominator)

Iterations = int(input("Enter number of iterations: "))

if Iterations >= 0:

    for count in range(iterations):

    SumApprox = SumApprox + (1/Denominator)

    Denominator = (Denominator + 2) * -1 

else:

    print("Number of iterations must be an integer greater than 0")

ValueofPi = SumApprox * 4

print("The approximate value of pi ", ValueofPi)
