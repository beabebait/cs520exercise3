from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    temp = ""
    balance = 0
    for char in paren_string:
        if char == ' ':
            continue
        temp += char
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            result.append(temp)
            temp = ""
    return result
