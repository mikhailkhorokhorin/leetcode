from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ls = [i for i in letters if i > target]
        return min(ls) if ls else letters[0]
