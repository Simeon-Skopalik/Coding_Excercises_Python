import pytest

from solutions import two_sum

def test_two_sum_finds_pair_at_start():
    nums = [2,7,11,15]
    target = 9

    result = two_sum(nums, target)

    assert sorted(result) == [0,1]

def test_two_sum_handles_duplicates():
    nums = [3,3]
    target = 6

    result = two_sum(nums, target)

    assert sorted(result) == [0,1]
  



     