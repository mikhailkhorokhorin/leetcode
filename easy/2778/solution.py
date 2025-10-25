from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum([nums[i - 1] ** 2 if n % i == 0 else 0 for i in range(1, n + 1)])
