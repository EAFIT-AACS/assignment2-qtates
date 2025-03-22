def validationString(correctStrings,worngStrings):
    vectorStrings=[]
    vectorStrings.append(correctStrings)
    vectorStrings.append(worngStrings)


    stack = ['b']
    q=vectorStrings[0]
    transitions = {("a","b"):"ab",("a","a"):"",("b",""):"b",("b","b"):"",("a",""):"abx",("a","x"):"ab"}

    for i in (vectorStrings):
        for j in range (len(vectorString)):
            letra = vectorStrings[j]
            stack2= stack.pop(0)

           

    return ":)"