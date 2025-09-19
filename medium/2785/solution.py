class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([char for char in s if char in "AEIOUaeiou"])
        res = list(s)
        index = 0
        for i, char in enumerate(res):
            if char in "AEIOUaeiou":
                res[i] = vowels[index]
                index += 1

        return "".join(res)
