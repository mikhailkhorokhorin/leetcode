from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        length = max([len(i) for i in s])
        res = ["" for _ in range(length)]

        for i in range(length):
            for word in s:
                if i < len(word):
                    res[i] += word[i]
                else:
                    res[i] += " "

        return [i.rstrip() for i in res]
