from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max(nums) if (nums := [i for i in set(arr) if i == arr.count(i)]) else -1
