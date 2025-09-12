class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        zx, zy = abs(z - x), abs(z - y)
        return 1 if zx > zy else 2 if zy > zx else 0
