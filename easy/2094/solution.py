from itertools import permutations
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()

        for p in permutations(digits, 3):
            if p[0] == 0 or p[-1] % 2 != 0:
                continue
            result.add(p[0] * 100 + p[1] * 10 + p[2])

        return sorted(result)
