class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if n < 10:
            return False
        count = 0
        while n > 0:
            temp = n % 10
            count += temp ** 2
            n //= 10
        return self.isHappy(count)
