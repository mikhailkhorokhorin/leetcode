from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        node = head
        next_greater = self.removeNodes(node.next)
        node.next = next_greater

        if not next_greater or node.val >= next_greater.val:
            return node

        return next_greater
