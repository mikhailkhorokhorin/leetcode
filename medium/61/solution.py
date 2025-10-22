from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        dummy = head
        length = 1

        while dummy.next:
            dummy = dummy.next
            length += 1

        if (k % length) == 0:
            return head

        cur = head
        for _ in range(length - (k % length) - 1):
            cur = cur.next

        new = cur.next
        cur.next = None
        dummy.next = head

        return new
