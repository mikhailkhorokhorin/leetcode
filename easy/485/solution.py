from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(j) for j in "".join([str(i) for i in nums]).split("0")])
