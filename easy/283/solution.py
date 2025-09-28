from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums[:] = [i for i in nums if i != 0] + [0] * nums.count(0)
