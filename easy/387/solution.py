import string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = [s.index(l) for l in string.ascii_lowercase if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
