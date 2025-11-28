from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(perm) for perm in set(permutations(nums))]
