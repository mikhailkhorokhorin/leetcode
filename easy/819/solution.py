from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        res = [
            i
            for i in re.findall(r"\b[a-z]+\b", paragraph.lower())
            if i not in set(banned)
        ]
        return max(res, key=res.count)
