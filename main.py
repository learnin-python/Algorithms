
"""
 Determine if Brackets are Balanced

from stack import Stack


# parent meaning parentheses



def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_parent_balanced(parent_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parent_string) and is_balanced:
        parent = parent_string[index]
        if parent in "([{":
            s.push(parent)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parent):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_parent_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_parent_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_parent_balanced("[][]"))


"""

# Reverse String

from stack import Stack


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push((input_str[i]))
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


stack = Stack()

input_str = "!ayneK ot emocleW"
print(reverse_string(stack, input_str))
