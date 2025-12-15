from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(nums[0::2]) - sum(nums[1::2])
