from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        l, r = dummy, dummy

        for _ in range(n + 1):
            l = l.next

        while l:
            l = l.next
            r = r.next

        r.next = r.next.next

        return dummy.next
