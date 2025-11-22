from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(0, 10 - i):
                num = int("123456789"[j : j + i])
                if low <= num <= high:
                    res.append(num)

        return res
