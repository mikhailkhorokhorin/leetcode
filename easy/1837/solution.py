class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = []

        while n > 0:
            res.append(int(n % k))
            n //= k

        return sum(res)
