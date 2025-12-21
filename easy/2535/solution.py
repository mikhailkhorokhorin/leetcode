from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for i in nums:
            for j in str(i):
                s2 += int(j)

        return abs(s1 - s2)
