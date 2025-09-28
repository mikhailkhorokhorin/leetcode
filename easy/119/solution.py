from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for num in range(rowIndex + 1):
            row = []
            for i in range(num + 1):
                if i == 0 or i == num:
                    row.append(1)
                else:
                    row.append(res[num - 1][i - 1] + res[num - 1][i])
            res.append(row)

        return res[rowIndex]
