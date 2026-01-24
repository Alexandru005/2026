# You are keeping the scores for a baseball game with strange rules.
# At the beginning of the game, you start with an empty record.
#
# Given a list of strings operations, where operations[i]
# is the ith operation you must apply to the record and is one of the following:
#
# An integer x: Record a new score of x.
# '+': Record a new score that is the sum of the previous two scores.
# 'D': Record a new score that is the double of the previous score.
# 'C': Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.


#My solution
def calPoints(operations):
    from functools import reduce
    lista = []
    l = 0
    for op in operations:
        if op == "+":
            lista.append(int(lista[-1]) + int(lista[-2]))
        elif op == "D":
            lista.append(int(lista[-1]) * 2)
        elif op == "C":
            lista.remove(lista[-1])
        else:
            lista.append(int(op))
    if lista == []:
        return 0
    return reduce(lambda x, y: x + y, lista)

print(calPoints(["5","-2","4","C","D","9","+","+"]))