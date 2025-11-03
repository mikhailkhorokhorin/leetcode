from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                if neededTime[i] < neededTime[i - 1]:
                    res += neededTime[i]
                    neededTime[i] = neededTime[i - 1]
                else:
                    res += neededTime[i - 1]

        return res
