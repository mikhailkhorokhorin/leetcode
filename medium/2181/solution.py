from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        count = 0
        while curr:
            if curr.val == 0:
                curr.val = count
                prev.next = curr
                prev = curr
                count = 0
            else:
                count += curr.val
            curr = curr.next

        return head.next
