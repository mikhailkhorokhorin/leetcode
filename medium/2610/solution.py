from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 0

            index = count[i]

            if index == len(res):
                res.append([])

            res[index].append(i)
            count[i] += 1

        return res
