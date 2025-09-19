from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        res = 0
        while l < r:
            height_l, height_r = height[l], height[r]
            res = max(res, (r - l) * min(height_l, height_r))
            if height_l < height_r:
                l += 1
            else:
                r -= 1

        return res
