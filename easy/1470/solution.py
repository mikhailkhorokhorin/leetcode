from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for a, b in zip(nums[:n], nums[n:]):
            res.extend([a, b])
        return res
