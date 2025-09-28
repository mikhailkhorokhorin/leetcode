from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        cookieIndex, childIndex = len(s) - 1, len(g) - 1

        while cookieIndex >= 0 and childIndex >= 0:
            if s[cookieIndex] >= g[childIndex]:
                res += 1
                cookieIndex -= 1
            childIndex -= 1

        return res
