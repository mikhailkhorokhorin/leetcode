from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            if i % 2 == 0:
                answer.append(i)
        for i in nums:
            if i % 2 != 0:
                answer.append(i)
        return answer
