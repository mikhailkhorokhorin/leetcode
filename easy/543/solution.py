from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node: Optional[TreeNode]):
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        depth(root)
        return self.diameter
