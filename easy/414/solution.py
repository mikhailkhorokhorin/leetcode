from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = sorted(set(nums))[-3:]
        return arr[0] if len(arr) > 2 else arr[-1]
