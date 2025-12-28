from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = [""]
        for c in target:
            res.append(new := res[-1] + "a")
            while new[-1] != c:
                next_char = "a" if new[-1] == "z" else chr(ord(new[-1]) + 1)
                new = new[:-1] + next_char
                res.append(new)
        return res[1:]
