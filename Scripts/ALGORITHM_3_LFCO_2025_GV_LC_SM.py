def printTree(results):
    word = results[3]
    tree = []
    stack = []
    rules = []
    for i in range(len(results[0])):
        if i == 0:
            rules.append("Original")
            stack.append(results[0][i])
            tree.append(word)
        else:
            rules.append(results[1][i-1])
            stack.append(results[0][i])
            tree.append(word)
        word = word[1:]
    if results[2] == 0:
        result = "The string belong to the language"
    else:
        result = "The string doesn't belong to the language"
    return tree, stack, rules, result