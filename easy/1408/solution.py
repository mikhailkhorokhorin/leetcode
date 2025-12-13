from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = " ".join(words)
        return [i for i in words if s.count(i) >= 2]
