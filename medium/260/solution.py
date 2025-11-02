from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [i for i in set(nums) if nums.count(i) == 1]
