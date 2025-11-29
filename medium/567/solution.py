class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, l = sorted(s1), len(s1)

        for i in range(len(s2) - l + 1):
            if sorted(s2[i : i + l]) == s1:
                return True
        return False
