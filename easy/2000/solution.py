class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = word.find(ch) + 1
        return word[:ind][::-1] + word[ind:]
