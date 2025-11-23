import pytest

# Import all four implementations
from problems.problem_3.problem_3_gpt_cot import separate_paren_groups as gpt_cot
from problems.problem_3.problem_3_gpt_selfdebug import separate_paren_groups as gpt_selfdebug
from problems.problem_3.problem_3_qwen_cot import separate_paren_groups as qwen_cot
from problems.problem_3.problem_3_qwen_selfdebug import separate_paren_groups as qwen_selfdebug

implementations = [gpt_cot, gpt_selfdebug, qwen_cot, qwen_selfdebug]


# ---------------------------------------------------------
# SPEC-GUIDED TESTS FOR PROBLEM 3
# ---------------------------------------------------------
@pytest.mark.parametrize("impl", implementations)
def test_no_spaces_in_output(impl):
    """Spec 1: Output groups contain no spaces."""
    s = "(()) () (()())"
    res = impl(s)
    assert all(" " not in group for group in res)


@pytest.mark.parametrize("impl", implementations)
def test_balanced_each_group(impl):
    """Spec 2: Every returned group must be a balanced parentheses string."""
    s = "() (()) (()())"
    res = impl(s)

    for group in res:
        # Balanced final depth
        final_depth = sum(1 if c == "(" else -1 for c in group)
        assert final_depth == 0

        # Never more closing than opening
        depth = 0
        for c in group:
            depth += 1 if c == "(" else -1
            assert depth >= 0


@pytest.mark.parametrize("impl", implementations)
def test_concatenation_equals_cleaned_input(impl):
    """Spec 3: Concatenating all groups equals input with spaces removed."""
    s = "  (()())   ()   (()) "
    clean = "".join(c for c in s if c != " ")
    assert all(ch in "()" for ch in clean) or clean == ""

    res = impl(s)
    assert "".join(res) == clean


@pytest.mark.parametrize("impl", implementations)
def test_groups_are_maximal(impl):
    """Spec 4: Groups must be maximal (cannot contain smaller balanced groups as separate entries)."""
    s = "() (()) (()())"
    res = impl(s)

    # A maximal group should not fully contain another distinct group as a substring
    for g1 in res:
        for g2 in res:
            if g1 != g2:
                assert not (g1 in g2)


@pytest.mark.parametrize("impl", implementations)
def test_group_count_matches_top_level_segments(impl):
    """Spec 5: Number of groups equals number of top-level balanced segments."""
    s = "() (()) (()()) ()"
    clean = "".join(c for c in s if c != " ")

    # Count top-level balanced groups
    depth = 0
    expected_groups = 0
    for ch in clean:
        if ch == "(":
            if depth == 0:
                expected_groups += 1
            depth += 1
        else:
            depth -= 1

    res = impl(s)
    assert len(res) == expected_groups

