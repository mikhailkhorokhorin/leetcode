from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = head

        while curr:
            curr_next = curr.next
            prev, next = res, res.next

            while next:
                if next.val > curr.val:
                    break
                prev = next
                next = next.next

            curr.next = next
            prev.next = curr
            curr = curr_next

        return res.next
