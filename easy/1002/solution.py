from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = set(words[0])
        res = []
        for letter in letters:
            count = min([words.count(letter) for word in words])
            if count:
                res += [letter] * count

        return res
