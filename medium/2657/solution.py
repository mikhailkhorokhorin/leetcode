from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []

        for i in range(len(A)):
            res.append(len(set(A[:i + 1]) & set(B[:i + 1])))

        return res
