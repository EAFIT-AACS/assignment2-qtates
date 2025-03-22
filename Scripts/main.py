import CreateStrings
import Automaton
import PrintTree

correctStrings=CreateStrings.createCorrectStrings()
worngStrings=CreateStrings.createWrongStrings()
print(correctStrings,worngStrings)

results=Automaton.validationString(correctStrings,worngStrings)

print(PrintTree.printTree(results))
palabra = "Hola".split(" ")
print(palabra)
for i in palabra:
    print(i)
    palabra.pop()