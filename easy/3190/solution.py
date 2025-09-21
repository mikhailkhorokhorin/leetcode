from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if i == 1 or i == 2:
                res += 1
            elif i % 3 == 0:
                continue
            elif i % 3 == 0 or i % 3 == 2:
                res += 1

        return res
