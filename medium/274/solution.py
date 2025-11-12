from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for i, c in enumerate(citations):
            if c < i + 1:
                break
            res = i + 1
        return res
