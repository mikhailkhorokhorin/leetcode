class Solution:
    def repeatedCharacter(self, s: str) -> str:
        chars = set()
        for i in s:
            if i not in chars:
                chars.add(i)
            else:
                return i
