import CreateStrings
import Automaton
import PrintTree

correctStrings=CreateStrings.createCorrectStrings()
worngStrings=CreateStrings.createWrongStrings()
print(correctStrings,worngStrings)

results=Automaton.validationString(correctStrings,worngStrings,0)

print(PrintTree.printTree(results))