from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length, res = len(mat), 0

        for i in range(length):
            res += mat[i][i] + mat[i][length - i - 1]

        if length % 2 == 1:
            res -= mat[length // 2][length // 2]

        return res
