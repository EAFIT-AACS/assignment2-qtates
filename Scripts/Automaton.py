def validationString(correctStrings,wrongStrings):
    
    # VectorString keeps the strings to be processed and adds the strings that belong and don't belong to the grammar's language definition.
    vectorStrings=[]
    vectorStrings.append(correctStrings)
    vectorStrings.append(wrongStrings)

    # Definition of automaton: Stack with its initial symbol, started state q, transitions).
    stack = ["b"]
    q=vectorStrings[0]
    #Definition of transitions/rules using a dictionary.
    functiontransition = {("a","b"):["ab",1],("a","a"):["",2],("b",""):["b",3],("b","b"):["",4],("a",""):["abx",5],("a","x"):["ab",6],("b","x"):["bx",7]}

    #Definition of the variable for having the sequence/steps of the stack and rule transition, necessary for the third algorithm.
    stackSequence=["b"]
    ruleTransitionsSequence=[]

    #Analizy every string in vectorStrings.
    for i in range(len(vectorStrings)):
        stack = ["b"] #In every iteration get the initial symbol in the stack.
        for j in range(len(vectorStrings[i])):
            letter=vectorStrings[i][j] #Processed letter for letter.
            
            if(len(stack) == 0):
                highStack=""
                stack.append(" ") #If the stack is empty, so add a (" ") to represent it and avoid issues.
            else:
                highStack= stack[0] #Otherwise take the first character in the stack.
            
            #Search the corresponding transition/rule for the letter and hihgStack, and add the number's rule.
            if (letter,highStack) in functiontransition:
                transition=functiontransition[letter,highStack][0]
                ruleTransitionsSequence.append(functiontransition[letter,highStack][1])
            else:
                #Not finding a transition with these values, so not exist and the string doesn't belong to the language.
                break
            print(letter,",",highStack,":",transition)
            
            #Delete the first character in the stack, and add the transition character to the character in the stack. When this process is finished add it stackSequence.
            stack.pop(0) 
            for k in range(len(transition)):
                stack.insert(k,transition[k])
            print(stack)
            stackSequence.append(stack[:])
        #If stack is empty, then the string was accepted.
        if len(stack)==0:
            print("The string belong to the language")
        else:
            print("The string doesn't belong to the language")

    return stackSequence, ruleTransitionsSequence

validationString("aaaabbbaaaabbbaabaabaaaabbb","aaab")