from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        points = [p1, p2, p3, p4]
        dist = []
        for i in range(4):
            for j in range(i + 1, 4):
                dist.append(
                    (points[i][0] - points[j][0]) ** 2
                    + (points[i][1] - points[j][1]) ** 2
                )

        dist.sort()

        return (
            dist[0] == dist[1] == dist[2] == dist[3]
            and dist[4] == dist[5]
            and dist[4] == 2 * dist[0]
            and dist[0] > 0
        )
