def validationString(correctStrings,wrongStrings):
    vectorStrings=[]
    vectorStrings.append(correctStrings)
    vectorStrings.append(wrongStrings)

    print(vectorStrings)

    stack = ["b"]
    q=vectorStrings[0]
    transitions = {("a","b"):"ab",("a","a"):"",("b",""):"b",("b","b"):"",("a",""):"abx",("a","x"):"ab"}

    caminoStack=["b"]
    caminoDerivacion=[]

    for i in range(len(vectorStrings)):
        for j in range(len(vectorStrings[i])):
            letra=vectorStrings[i][j]
            stack2= stack[0]
            transicion=transitions[letra,stack2]
            print(letra,",",stack2,":",transicion)
            stack.pop(0)
            #for k in range(len(transicion)-1,-1,-1):
                #stack.insert(0,transicion[k])
            #print(stack)
                

        print()

    return ":)"



validationString("abaa","aaab")