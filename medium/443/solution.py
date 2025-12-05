from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        res = []
        prev = chars[0]
        cur = 1

        for i in range(1, len(chars)):
            if chars[i] == prev:
                cur += 1
            else:
                res.append(prev)
                if cur > 1:
                    for j in str(cur):
                        res.append(j)

                prev = chars[i]
                cur = 1
        if prev:
            res.append(prev)
            if cur > 1:
                for j in str(cur):
                    res.append(j)

        for i in range(len(chars)):
            chars[i] = res[i]

        return len(res)
