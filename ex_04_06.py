# Rewrite your pay computation with time-and-a-half
# for overtime and create a function called computepay
# which takes two parameters (hours and rate)

def computepay(hours, rate):
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

    return pay

hrs = input("Enter number of hours worked: ")
rt = input("Enter rate per hour: ")

pay = computepay(hrs, rt)
print("Pay", pay)