from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        arr[:] = [int(j) for j in "".join([str(i) for i in arr]).replace("0", "00")][:len(arr)]
