from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if words[i].count(x) != 0]
