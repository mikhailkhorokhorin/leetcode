from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children


class Solution:
    def dfs(self, root: "Node", res: List[int]):
        for child in root.children:
            self.dfs(child, res)
        res.append(root.val)

    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        res = []
        self.dfs(root, res)
        return res
