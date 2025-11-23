from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in matrix:
            res.extend(i)
        return sorted(res)[k - 1]
