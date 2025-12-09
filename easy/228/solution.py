from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = []

        for i in nums:
            if r and r[-1][1] == i - 1:
                r[-1][1] = i
            else:
                r.append([i, i])

        return [f"{x}->{y}" if x != y else f"{x}" for x, y in r]
