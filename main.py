import CreateStrings
import Automaton
import PrintTree

correctStrings=CreateStrings.createCorrectStrings()
worngStrings=CreateStrings.createWorngStrings()
print(correctStrings,worngStrings)

results=Automaton.validationString(correctStrings,worngStrings)

print(PrintTree.PrintTree(results))