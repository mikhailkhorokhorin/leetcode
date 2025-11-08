class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        s1_breaks_s2 = s2_breaks_s1 = True

        for i in range(len(s1)):
            if s1[i] < s2[i]:
                s1_breaks_s2 = False
            if s2[i] < s1[i]:
                s2_breaks_s1 = False

        return s1_breaks_s2 or s2_breaks_s1
