from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(i for i in nums if nums.count(i) == 1)
        return nums.index(m) if all(m >= 2 * num for num in nums if m != num) else -1
