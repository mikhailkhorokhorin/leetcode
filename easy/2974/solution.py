from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while nums:
            nums.remove(a := min(nums))
            nums.remove(b := min(nums))
            arr.append(b)
            arr.append(a)
        return arr
