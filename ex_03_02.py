# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
hours = input("Enter number of hours worked: ")
rate = input("Enter rate per hour: ")

try:
    h = float(hours)
    r = float(rate)
except:
    print("Error, please enter numeric input.")
    quit()

if h > 40:
    reg_pay = h * r
    ot_pay = (h - 40.0) * (r * 0.5)
    pay = reg_pay + ot_pay
else:
    pay = h * r

print('Pay:', pay)