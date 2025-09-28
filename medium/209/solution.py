from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total, result = 0, 0, float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if result == float("inf") else result
