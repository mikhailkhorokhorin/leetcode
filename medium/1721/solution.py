from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head

        length = 0
        while dummy:
            length += 1
            dummy = dummy.next

        first, second = head, head
        for _ in range(k - 1):
            first = first.next
        for _ in range(length - k):
            second = second.next

        first.val, second.val = second.val, first.val
        return head
