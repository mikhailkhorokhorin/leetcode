from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(n1, n2, level):
            if not n1 or not n2:
                return
            if level % 2 != 0:
                n1.val, n2.val = n2.val, n1.val

            dfs(n1.left, n2.right, level + 1)
            dfs(n2.left, n1.right, level + 1)

        dfs(root.left, root.right, 1)
        return root
