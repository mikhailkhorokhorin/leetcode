from itertools import permutations
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return any(v == 2 * u for v, u in permutations(arr, 2))
