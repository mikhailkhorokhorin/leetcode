class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        temp, res = 1, 2
        for i in range(3, n + 1):
            temp, res = res, temp + res
        return res
