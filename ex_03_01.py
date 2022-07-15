# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = input("Enter number of hours worked: ")
rate = input("Enter rate per hour: ")
h = float(hours)
r = float(rate)

if h > 40:
    reg_pay = h * r
    ot_pay = (h - 40.0) * (r * 0.5)
    pay = reg_pay + ot_pay
else:
    pay = h * r

print('Pay:', pay)