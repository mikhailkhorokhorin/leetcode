from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            res["".join(sorted(i))].append(i)

        return list(res.values())
