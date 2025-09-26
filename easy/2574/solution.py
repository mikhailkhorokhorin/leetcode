from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(abs(sum(nums[:i]) - sum(nums[i + 1:])))

        return result
