from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = {}
        for index, value in enumerate(nums):
            if value in res and index - res[value] <= k:
                return True
            res[value] = index
        return False
