from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [
            i
            for i in words
            if len(i) == len(pattern)
            and len(set(i)) == len(set(pattern))
            and len(set(zip(i, pattern))) == len(set(i))
        ]
