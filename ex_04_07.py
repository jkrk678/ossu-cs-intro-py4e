# Rewrite the grade program from the previous chapter
# using a function called computegrade that takes
# a score as its parameter and returns
# a grade as a string

def computegrade(score):
    try:
        s = float(score)
    except:
        return "Bad score"

    if s < 0.0 or s > 1.0:
        return "Bad score"
    else:
        if s >= 0.9: return 'A'
        elif s >= 0.8: return 'B'
        elif s >= 0.7: return 'C'
        elif s >= 0.6: return 'D'
        else: return 'F'

sc = input("Enter score between 0.0 and 1.0: ")

my_score = computegrade(sc)
print("Score:", my_score)