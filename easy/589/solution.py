from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children


class Solution:
    def dfs(self, root: "Node", res: List[int]):
        if root is None:
            return
        res.append(root.val)
        for child in root.children:
            self.dfs(child, res)

    def preorder(self, root: "Node") -> List[int]:
        res = []
        self.dfs(root, res)
        return res
