# Write another program that prompts for a list of
# numbers as above and at the end prints out both
# the maximum and minimum of the numbers instead
# of the average.

min = None
max = None

while True:
    inp = input("> ")
    if inp == 'done':
        break

    try:
        num = int(inp)
    except:
        print("Invalid input")
        continue

    if min is None or num < min:
        min = num
    if max is None or num > max:
        max = num

print('Maximum is', max)
print('Minimum is', min)