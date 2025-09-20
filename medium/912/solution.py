from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def max_heapify(heap_size, index):
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            if largest != index:
                nums[index], nums[largest] = nums[largest], nums[index]
                max_heapify(heap_size, largest)

        for i in range(len(nums) // 2 - 1, -1, -1):
            max_heapify(len(nums), i)

        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            max_heapify(i, 0)

        return nums
