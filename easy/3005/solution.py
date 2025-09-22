from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = {i: nums.count(i) for i in set(nums)}
        max_frequency = max(frequency.values())
        return sum([i for i in frequency.values() if i == max_frequency])
