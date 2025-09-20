from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        ls = []
        while temp:
            ls.append(temp.val)
            temp = temp.next

        ls.sort()

        temp = head
        for i in range(len(ls)):
            temp.val = ls[i]
            temp = temp.next

        return head
