# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

cel = input("Enter degress Celsius: ")
c = float(cel)
f = c * 9 / 5 + 32
print(cel, 'degrees Celsius is', f, 'degrees Fahrenheit')