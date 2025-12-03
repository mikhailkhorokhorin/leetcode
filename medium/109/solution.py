from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head

        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next

        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(
                nodes[mid], buildBST(left, mid - 1), buildBST(mid + 1, right)
            )

            return node

        return buildBST(0, len(nodes) - 1)
