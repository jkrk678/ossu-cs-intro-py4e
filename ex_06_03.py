# Encapsulate this code in a function named count,
# and generalize it so that it accepts the
# string and the letter as arguments.

def count(str, char):
    count = 0
    for letter in str:
        if letter == char:
            count = count + 1
    return count

aInBanana = count('banana', 'a')
print(aInBanana)