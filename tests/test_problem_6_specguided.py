import pytest
from problems.problem_6.problem_6_gpt_cot import mean_absolute_deviation as gpt_cot
from problems.problem_6.problem_6_gpt_selfdebug import mean_absolute_deviation as gpt_selfdebug
from problems.problem_6.problem_6_qwen_cot import mean_absolute_deviation as qwen_cot
from problems.problem_6.problem_6_qwen_selfdebug import mean_absolute_deviation as qwen_selfdebug

impls = [gpt_cot, gpt_selfdebug, qwen_cot, qwen_selfdebug]


@pytest.mark.parametrize("impl", impls)
def test_mad_non_negative(impl):
    # Spec 1: MAD must always be >= 0
    assert impl([3, 7, 11]) >= 0
    assert impl([-10, -20, -30]) >= 0


@pytest.mark.parametrize("impl", impls)
def test_mad_empty_list_zero(impl):
    # Spec 2: MAD([]) == 0
    assert impl([]) == 0


@pytest.mark.parametrize("impl", impls)
def test_mad_identical_values_zero(impl):
    # Spec 3: All identical → MAD = 0
    assert impl([5, 5, 5, 5]) == 0
    assert impl([-3.2, -3.2]) == 0


@pytest.mark.parametrize("impl", impls)
def test_mad_matches_definition(impl):
    # Spec 4: Definition-based calculation
    nums = [2.0, 4.0, 6.0, 8.0]
    mean = sum(nums) / len(nums)
    expected = sum(abs(x - mean) for x in nums) / len(nums)
    assert impl(nums) == expected

    nums2 = [-1.0, 1.0, -2.0, 2.0]
    mean2 = sum(nums2) / len(nums2)
    expected2 = sum(abs(x - mean2) for x in nums2) / len(nums2)
    assert impl(nums2) == expected2


@pytest.mark.parametrize("impl", impls)
def test_mad_invariant_under_shift(impl):
    # Spec 5: MAD invariant under adding constant k
    nums = [10.0, 12.0, 14.0]
    result_original = impl(nums)

    k = 5.0
    nums_shifted = [x + k for x in nums]
    result_shifted = impl(nums_shifted)

    assert result_original == result_shifted
