from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(task[0] + task[1] for task in tasks)
