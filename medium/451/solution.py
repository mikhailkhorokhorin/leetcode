class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {i: s.count(i) for i in set(s)}
        sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
        return "".join([key * val for key, val in sorted_chars])
