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
# Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha válida (día, mes, año). Devolver True o False según
# la fecha sea correcta o no.
def leapYear(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 4 != 0:
        return False

def validDate(day, month, year):
    if leapYear(year):
        februaryDays = 29
    else:
        februaryDays = 28
    validDaysForMonths = {
                            1: 31,
                            2: februaryDays,
                            3: 31,
                            4: 30,
                            5: 31,
                            6: 30,
                            7: 31,
                            8: 31,
                            9: 30,
                            10: 31,
                            11: 30,
                            12: 31
                            }
    if day <= 0 or month < 1 or year <= 0:
        return False
    if validDaysForMonths.get(month) >= day:
        return True
    else:
        return False
assert(not validDate(-1, 5, 2002))
assert(validDate(30, 3, 2000))
assert(validDate(29, 2, 2000))
assert(not validDate(29, 2, 2001))