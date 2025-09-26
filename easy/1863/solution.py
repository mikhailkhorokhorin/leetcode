from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result |= i
        return result * (1 << (len(nums) - 1))
