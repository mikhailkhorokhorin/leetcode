from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        l = []
        for i in strs:
            l.append(int(i) if i.isdigit() else len(i))
        return max(l)
