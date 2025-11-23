import pytest
from problems.problem_3.problem_3_gpt_cot import separate_paren_groups


# ----------------------------------------------------------
# 1. No output group contains spaces
# ----------------------------------------------------------
def test_no_group_contains_spaces_spec():
    s = "(()) () ((()))"
    res = separate_paren_groups(s)
    assert all(" " not in group for group in res)


# ----------------------------------------------------------
# 2. Every returned group is a balanced parentheses string
# ----------------------------------------------------------
def test_groups_are_balanced_spec():
    s = "()(())(()())"
    res = separate_paren_groups(s)

    def is_balanced(group):
        # total balance must be 0
        if sum(1 if c == "(" else -1 for c in group) != 0:
            return False
        # prefixes must not dip negative
        bal = 0
        for c in group:
            bal += 1 if c == "(" else -1
            if bal < 0:
                return False
        return True

    assert all(is_balanced(group) for group in res)


# ----------------------------------------------------------
# 3. Concatenation of groups must equal the input stripped of spaces
# ----------------------------------------------------------
def test_groups_concatenate_to_clean_string_spec():
    s = " () (())   (()()) "
    clean = "".join(c for c in s if c != " ")

    res = separate_paren_groups(s)

    # clean should contain only parentheses
    assert all(ch in "()" for ch in clean) or clean == ""
    assert "".join(res) == clean


# ----------------------------------------------------------
# 4. Each group is maximal — cannot be decomposed into subgroups
# ----------------------------------------------------------
def test_groups_are_maximal_spec():
    s = "() (()) (()())"
    res = separate_paren_groups(s)

    for g in res:
        # A proper substring that is balanced should NOT exist inside g
        # except empty / the whole string
        for i in range(1, len(g)-1):
            for j in range(i+1, len(g)):
                sub = g[i:j]

                # check if sub is balanced
                bal = sum(1 if c == "(" else -1 for c in sub)
                prefix_ok = all(
                    (1 if sub[k] == "(" else -1)
                    + sum(1 if c == "(" else -1 for c in sub[:k])
                    >= 0
                    for k in range(len(sub))
                )

                if bal == 0 and prefix_ok:
                    # found a smaller balanced group → violation
                    assert False, f"Group {g} contains smaller balanced group {sub}"

    assert True  # If no violation occurred


# ----------------------------------------------------------
# 5. Number of groups equals number of top-level balanced segments
# ----------------------------------------------------------
def test_number_of_groups_matches_top_level_segments_spec():
    s = "(())()(()) (()())"
    clean = "".join(c for c in s if c != " ")

    # count top-level balanced segments
    depth = 0
    expected_count = 0
    for ch in clean:
        if ch == "(":
            if depth == 0:
                expected_count += 1
            depth += 1
        else:
            depth -= 1

    res = separate_paren_groups(s)
    assert len(res) == expected_count
