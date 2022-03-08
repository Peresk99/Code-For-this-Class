HourlyWage = float(input("Enter the hourly pay : $"))
Hours = float(input("Enter the amount of hours worked: "))
Overtime = float(input("Enter the overtime hours worked: "))
OvertimePay = Overtime * 1.5
print("Overtime pay is $" + str(OvertimePay))
TotalPay = HourlyWage * Hours + OvertimePay
print("The total weekly pay is $" + str(TotalPay))
