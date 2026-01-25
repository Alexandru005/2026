# You are given a string s consisting of the following characters:
# '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# My solution
def isValid(s):
    if len(s) <= 1:
        return False
    list = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            list.append(char)
        else:
            if list == []:
                return False
            if ((list[-1] == '(' and char != ')') or (list[-1] == '[' and char != ']') or (list[-1] == '{' and char != '}')):
                return False
            list.pop()
    if list != []:
        return False
    return True

print(isValid("]]"))