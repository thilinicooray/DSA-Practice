

def valid_parentheses(s: str) -> bool:
    if not s:
        return False

    para_dict = {'}':'{', ']':'[',')':'('}

    if s[0] in para_dict:
        return False

    stack = []

    for char in s:
        if char in para_dict:
            prev = stack.pop()

            if prev != para_dict[char]:
                return False

        else:
            stack.append(char)

    return True if not stack else False