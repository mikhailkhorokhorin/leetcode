class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        div = {
            i
            for d in range(2, int(num ** 0.5) + 1)
            if num % d == 0
            for i in (d, num // d)
        }
        return num == sum(div) + 1
