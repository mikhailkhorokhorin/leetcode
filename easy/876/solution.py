from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle, end = head, head

        while end is not None and end.next is not None:
            middle = middle.next
            end = end.next.next

        return middle
