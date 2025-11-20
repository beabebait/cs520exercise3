from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    processed_str = paren_string.replace(' ', '')
    groups = []
    balance = 0
    start = 0
    for i, char in enumerate(processed_str):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            groups.append(processed_str[start:i+1])
            start = i + 1
    return groups
