from itertools import product


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        i = 0
        for p in product(["a", "b", "c"], repeat=n):
            p = "".join(p)
            if "aa" not in p and "bb" not in p and "cc" not in p:
                i += 1
                if i == k:
                    return p

        return ""


print(Solution().getHappyString(n=1, k=3))
