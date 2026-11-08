import pytest
import logging

from solutions import two_sum, top_k_frequent
from audit import AuditLog

### Two Sum Tests ### ----------------------------------------
@pytest.mark.parametrize("nums, target, expected",[
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
    ([-1, -2, -3], -5, [1, 2])
],
ids=["basic_case", "no_self_reuse", "equal_values", "negative_numbers"]
)
def test_two_sum_parametrized(nums, target, expected):
    assert sorted(two_sum(nums,target)) == expected

def test_two_sum_no_solution():
    with pytest.raises(ValueError):
        two_sum([1,2,3], 100)


### Top K Frequent Tests ### -----------------------------------------------
def test_top_k_frequent_basic():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

def test_top_k_larger_than_distinct():
    nums  = [1, 1, 2]
    k = 5

    result = top_k_frequent(nums, k)

    assert sorted(result) == sorted(set(nums))

@pytest.mark.parametrize("nums, k, expected",[
    ([1],1,[1]),
    ([],2,[])
],
ids=["single_element","empty_list"])
def test_top_k_frequent_edge_cases(nums, k, expected):
    assert top_k_frequent(nums, k) == expected



### Audit Log Test ### --------------------------------------------------------

def test_audit_log_prints_start_and_end(caplog):
    with caplog.at_level(logging.INFO):
        with AuditLog("job"):
            pass

    messages = [record.getMessage() for record in caplog.records]

    assert messages == ["START job", "END job"]


def test_audit_log_records_failures(caplog):
        with caplog.at_level(logging.INFO):
            with pytest.raises(ValueError):
                with AuditLog("job"):
                    raise ValueError("bad price")

        messages = [record.getMessage() for record in caplog.records]

        assert messages == ["START job", "FAILED job: bad price"]
        assert caplog.records[-1].levelno == logging.ERROR



    