import random as r

# Function to generate Right strings (acpeted by the automaton)
def createCorrectStrings():
    strings = []
    for i in range (r.randint(2,3)):
        cadena = ""
        # Generate a random number of sets of strings to concatenate in a complete string
        stringAmounts = r.randint(1,4)
        # If the number of strings is even, add one to make it odd
        if stringAmounts%2 == 0:
            stringAmounts += 1
        for k in range (stringAmounts):
            # Generate a random number of "a" to concatenate
            aAmounts = r.randint(1,5)
            # If the number of "a" is odd, add one to make it even
            if aAmounts%2 != 0:
                aAmounts += 1
            # Generate a random number of "b" to concatenate
            bAmounts = r.randint(1,4)
            # If the number of "b" is even, add one to make it odd
            if bAmounts%2 == 0:
                bAmounts += 1
            for j in range (aAmounts):
                cadena += "a"
            for j in range (bAmounts):
                cadena += "b"
        # Append the string to the list of strings
        strings.append(cadena)
    return strings

# Function to generate Wrong strings (rejected by the automaton)
def createWrongStrings():
    strings = []
    for i in range (r.randint(2,3)):
        cadena = ""
        # Generate a random number of sets of strings to concatenate in a complete string
        stringAmounts = r.randint(1,4)
        # If the number of strings is odd, add one to make it even (to secure that the string is going to be rejected by the automaton)
        if stringAmounts%2 != 0:
            stringAmounts += 1
        # Generate a random number of "a" and "b" to concatenate without any restriction
        for k in range (stringAmounts):
            aAmounts = r.randint(1,6)
            bAmounts = r.randint(1,7)
            for j in range (aAmounts):
                cadena += "a"
            for j in range (bAmounts):
                cadena += "b"
        # Append the string to the list of strings
        strings.append(cadena)
    return strings