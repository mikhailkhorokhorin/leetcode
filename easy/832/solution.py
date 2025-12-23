from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l, r = 0, len(i) - 1
            while l < r:
                i[l], i[r] = i[r], i[l]
                l += 1
                r -= 1

        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] = int(image[i][j] == 0)
        return image
