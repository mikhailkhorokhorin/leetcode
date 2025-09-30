class Solution:
    def clearDigits(self, s: str) -> str:
        res = ""
        for i in s:
            if i.isdigit():
                if res:
                    res = res[:-1]
            else:
                res += i

        return res
