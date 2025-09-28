def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            middle = (l + r) // 2
            res = guess(middle)
            if res == 0:
                return middle

            if res == -1:
                r = middle - 1
            else:
                l = middle + 1
