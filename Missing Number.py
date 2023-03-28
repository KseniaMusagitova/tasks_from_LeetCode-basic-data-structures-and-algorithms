

import pytest


class Solution:
    def missingNumber(self, nums) -> int:
        sum_num = sum(nums)
        sum_total = ((0 + len(nums)) * (len(nums) + 1)) // 2
        return sum_total - sum_num


sol = Solution()


@pytest.mark.parametrize("nums, answer", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
])
def test_solution(nums, answer):
    assert sol.missingNumber(nums) == answer

