from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        h = {}

        for i in nums:
            h[i] = h.get(i, 0) + 1
            if h[i] == n:
                return i
        return -1
