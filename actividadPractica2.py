# %%
# 1. Desarrollar una función que reciba tres números positivos y devuelva el mayor
# de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor
# estricto devolver -1.
def biggerNumber(*numbers):
    listOfNumbers = list(numbers)
    listOfNumbers.sort()
    biggerElement = listOfNumbers[-1]
    if listOfNumbers.count(biggerElement) == 1:
        return biggerElement
    else: return -1
assert(biggerNumber(1, 5, 2, 4, 12) == 12)
assert(biggerNumber(12, 5, 2, 4, 12) == -1)

# %%
