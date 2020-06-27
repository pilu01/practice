import pytest
from letcode import *


@pytest.mark.parametrize('nums, target, result', [([1,1,2],2,[0,1]), ([-1,-2,4],2,[1,2])])
def test_two_sum(nums, target, result):
    assert two_sum(nums, target) == result