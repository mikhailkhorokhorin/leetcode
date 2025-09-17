class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "")
        res = []
        i = 0
        length = len(number)
        while i < length:
            if i + 4 == length:
                res.append(number[i:i + 2])
                i += 2
            if i + 3 <= length:
                res.append(number[i:i + 3])
                i += 3
            else:
                res.append(number[i:i + 2])
                i += 2

        if len(res) > 1:
            return "-".join(res)

        return res[0]
