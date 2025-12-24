class Solution:
    def hasSameDigits(self, s: str) -> bool:
        res = list(map(int, s))
        while len(res) > 2:
            temp = []
            for i in range(len(res) - 1):
                temp.append((res[i] + res[i + 1]) % 10)
            res = temp
        return res[0] == res[1]
