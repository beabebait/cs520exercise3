import pytest
from problems.problem_3.problem_3_gpt_cot import separate_paren_groups as gpt_cot
from problems.problem_3.problem_3_gpt_selfdebug import separate_paren_groups as gpt_selfdebug
from problems.problem_3.problem_3_qwen_cot import separate_paren_groups as qwen_cot
from problems.problem_3.problem_3_qwen_selfdebug import separate_paren_groups as qwen_selfdebug

@pytest.mark.parametrize("impl", [gpt_cot, gpt_selfdebug, qwen_cot, qwen_selfdebug])
def test_separate_paren_groups(impl):
    assert impl("()(( ))(( )( ))") == ['()', '(())', '(()())']
    assert impl("") == []
    assert impl("()") == ['()']
    assert impl("((()))") == ['((()))']

    #added from iteration 1
    assert impl("()()()") == ['()', '()', '()']  # consecutive simple pairs
    assert impl("((())())") == ['((())())']      # nested mix
    assert impl("(())(())") == ['(())', '(())']  # multiple nested groups
    assert impl("   ") == []                     # only spaces
    assert impl("()(( ) )") == ['()', '(())']    # nested with spaces

    # added from iteration 2
    # empty parentheses inside another group
    assert impl("()()((())())") == ['()', '()', '((())())']
    # deeply nested empty groups
    assert impl("(((())))") == ['(((())))']
    # multiple adjacent empty groups
    # dupe: assert impl("()()()") == ['()', '()', '()']

    # added from iteration 3
    # multiple consecutive empty groups with spaces
    assert impl("() () ()") == ['()', '()', '()']
    # nested empty groups with other content
    assert impl("((())())()") == ['((())())', '()']
    # leading and trailing spaces
    assert impl("   ()(())   ") == ['()', '(())']
    # empty inside nested non-empty groups
    assert impl("((()()))") == ['((()()))']
