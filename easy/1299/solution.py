from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in reversed(range(len(arr))):
            current = arr[i]
            arr[i] = greatest
            if current > greatest:
                greatest = current
        return arr
