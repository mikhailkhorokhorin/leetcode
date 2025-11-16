class Solution:
    def numSub(self, s: str) -> int:
        res = cur = 0
        for c in s:
            cur = cur + 1 if c == "1" else 0
            res = (res + cur) % (10**9 + 7)
        return res
