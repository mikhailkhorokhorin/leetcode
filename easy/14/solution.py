from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in strs[0]:
            res += i
            if sum([1 if word.startswith(res) else 0 for word in strs]) != len(strs):
                return res[:-1]
        return res
