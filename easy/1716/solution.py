class Solution:
    def totalMoney(self, n: int) -> int:
        total, mondayVal = 0, 1

        for i in range(1, n + 1):
            total += mondayVal + (i - 1) % 7
            if i % 7 == 0:
                mondayVal += 1
        return total


Solution().totalMoney(10)
