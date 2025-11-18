from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        s = set()

        for i in nums:
            if i not in s:
                s.add(i)
            else:
                res.append(i)

        return res
