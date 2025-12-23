from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen, count = set(), 0
        for i in nums:
            if i - diff in seen and i - diff * 2 in seen:
                count += 1
            seen.add(i)
        return count
