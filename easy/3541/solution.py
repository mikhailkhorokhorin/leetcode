class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels, consonant = {}, {}

        for i in s:
            if i in "aeiou":
                vowels[i] = vowels.get(i, 0) + 1
            else:
                consonant[i] = consonant.get(i, 0) + 1

        return max(vowels.values(), default=0) + max(consonant.values(), default=0)
