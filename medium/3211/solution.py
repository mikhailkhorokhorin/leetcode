from itertools import product
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        for i in product(["0", "1"], repeat=n):
            s = "".join(i)
            if "00" not in s:
                res.append(s)

        return res
