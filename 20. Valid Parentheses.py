from timeit import timeit

string = "[[]]{}"
lettermap = {"]": "[",
             ")": "(",
             "}": "{"}


def valid_parenthesis_issac(string, lettermap):
    stack = []
    for letter in string:
        if letter not in lettermap:
            stack.append(letter)
        else:
            if len(stack) == 0:
                return False
            pop_result = stack.pop()
            if lettermap[letter] != pop_result:
                return False
    if len(stack) != 0:
        return False
    return True


# possible online solution
def valid_parenthesis_online(s: str) -> bool:
    paren_stack = []
    for c in s:
        if c in ['(', '{', '[']:
            paren_stack.append(c)
        elif c == ')':
            if not paren_stack or paren_stack[-1] != '(':
                return False
            else:
                del paren_stack[-1]
        elif c == '}':
            if not paren_stack or paren_stack[-1] != '{':
                return False
            else:
                del paren_stack[-1]
        elif c == ']':
            if not paren_stack or paren_stack[-1] != '[':
                return False
            else:
                del paren_stack[-1]
    return (paren_stack == [])
