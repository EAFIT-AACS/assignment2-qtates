import random as r

def createCorrectStrings():
    strings = []
    for i in range (r.randint(2,5)):
        cadena = ""
        stringAmounts = r.randint(1,4)
        if stringAmounts%2 == 0:
            stringAmounts += 1
        for k in range (stringAmounts):
            aAmounts = r.randint(1,6)
            if aAmounts%2 != 0:
                aAmounts += 1
            bAmounts = r.randint(1,7)
            if bAmounts%2 == 0:
                bAmounts += 1
            for j in range (aAmounts):
                cadena += "a"
            for j in range (bAmounts):
                cadena += "b"
        strings.append(cadena)
    return strings

def createWorngStrings():
    strings = []
    for i in range (r.randint(2,5)):
        cadena = ""
        stringAmounts = r.randint(1,4)
        if stringAmounts%2 != 0:
            stringAmounts += 1
        for k in range (stringAmounts):
            aAmounts = r.randint(1,6)
            bAmounts = r.randint(1,7)
            for j in range (aAmounts):
                cadena += "a"
            for j in range (bAmounts):
                cadena += "b"
        strings.append(cadena)
    return strings