from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[min_index], nums[i] = nums[i], nums[min_index]
