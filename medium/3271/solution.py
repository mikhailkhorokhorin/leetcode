class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), k):
            result += chr((sum(ord(j) - 97 for j in s[i: i + k]) % 26) + 97)
        return result
