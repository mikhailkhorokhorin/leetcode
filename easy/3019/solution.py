class Solution:
    def countKeyChanges(self, s: str) -> int:
        low = s.lower()
        count = 0
        for ch in range(0, len(low) - 1):
            if low[ch] != low[ch + 1]:
                count += 1
        return count
