from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        count = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if prev != nums[i]:
                count = 0
            else:
                count += 1

            if count <= 1:
                nums[index] = nums[i]
                index += 1
                prev = nums[i]

        return index
