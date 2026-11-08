import pytest

from solutions import two_sum


@pytest.mark.parametrize("nums, target, expected",[
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
],
ids=["basic_case", "no_self_reuse", "equal_values"]
)
def test_two_sum_parametrized(nums, target, expected):
    assert sorted(two_sum(nums,target)) == expected

