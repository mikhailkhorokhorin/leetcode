from itertools import combinations
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(i + j < target for i, j in combinations(nums, 2))
