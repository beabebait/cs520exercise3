import pytest
from problems.problem_6.problem_6_gpt_cot import mean_absolute_deviation as gpt_cot
from problems.problem_6.problem_6_gpt_selfdebug import mean_absolute_deviation as gpt_selfdebug
from problems.problem_6.problem_6_qwen_cot import mean_absolute_deviation as qwen_cot
from problems.problem_6.problem_6_qwen_selfdebug import mean_absolute_deviation as qwen_selfdebug

@pytest.mark.parametrize("impl", [gpt_cot, gpt_selfdebug, qwen_cot, qwen_selfdebug])
def test_mean_absolute_deviation(impl):
    assert impl([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert impl([5.0, 5.0, 5.0]) == 0.0
    assert impl([]) == 0.0
    assert round(impl([1.0, 3.0]), 6) == 1.0

    # added for iteration 1
   # dupe: assert impl([]) == 0.0                        # empty list, avoid ZeroDivisionError
    assert impl([7.0]) == 0.0                     # single element
    assert impl([-1.0, 1.0, -1.0, 1.0]) == 1.0   # mix of positive/negative
    assert impl([0.0, 0.0, 0.0]) == 0.0          # all zeros
    assert impl([1e6, 1e6+1, 1e6+2]) == 0.6666666666666666  # large numbers
