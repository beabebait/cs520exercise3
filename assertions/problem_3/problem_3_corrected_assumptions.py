# 1. The output must contain no spaces because spaces in the input are ignored.
assert all(" " not in group for group in res)

# 2. Every returned group must be a balanced parentheses string.
assert all(
    sum(1 if c == "(" else -1 for c in group) == 0
    and all(group[:i].count("(") >= group[:i].count(")") for i in range(len(group)))
    for group in res
)

# 3 (Corrected). Concatenating all groups (in order) must equal the input string with all spaces removed.
clean = "".join(c for c in paren_string if c != " ")
assert all(ch in "()" for ch in clean) or clean == ""
assert "".join(res) == clean


# 4 (Corrected). Each group must be a *maximal* balanced group:  
#    no group can be split into two smaller balanced groups.
assert all(
    not (group1 != group2 and group1 in group2)
    for group1 in res for group2 in res
)


# 5. The number of groups equals the number of top-level balanced segments in the space-stripped input.
clean = "".join(c for c in paren_string if c != " ")
depth = 0
count = 0
for ch in clean:
    if ch == "(":
        if depth == 0:
            count += 1
        depth += 1
    else:
        depth -= 1
assert len(res) == count
