# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input("Enter number of hours worked: ")
rate = input("Enter rate per hour: ")
h = float(hours)
r = float(rate)
print('Pay:', r * h)