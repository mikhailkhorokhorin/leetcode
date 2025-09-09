from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([1 if i % 2 != 0 else 0 for i in nums])
