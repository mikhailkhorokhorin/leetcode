from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        s = "".join([str(i % 2) for i in nums])
        return "00" not in s and "11" not in s
