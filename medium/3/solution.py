class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        res = 0

        for i in range(length):
            seen = set()
            for j in range(i, length):
                if s[j] in seen:
                    break

                seen.add(s[j])
                res = max(res, j - i + 1)

        return res
