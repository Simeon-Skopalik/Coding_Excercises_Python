import pytest

from solutions import two_sum


"""
### Unit Tests Archive

def test_two_sum_basic_case():
    nums = [2,7,11,15]
    target = 9

    result = two_sum(nums, target)

    assert sorted(result) == [0,1]

def test_two_sum_does_not_reuse_same_element():
    nums = [3,2,4]
    target = 6

    result = two_sum(nums, target)

    assert sorted(result) == [1,2]

def test_two_sum_finds_pairs_of_equal_values():

    nums = [3,3]
    target = 6

    result = two_sum(nums, target)

    assert sorted(result) == [0,1]
"""


@pytest.mark.parametrize("nums, target, expected",[
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
],
ids=["basic_case", "no_self_reuse", "equal_values"]
)
def test_two_sum_parametrized(nums, target, expected):
    assert sorted(two_sum(nums,target)) == expected

