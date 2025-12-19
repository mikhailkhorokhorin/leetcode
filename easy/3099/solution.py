class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        return res if x % (res := sum([int(i) for i in str(x)])) == 0 else -1
