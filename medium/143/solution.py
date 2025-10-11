from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head

        middle, fast = head, head.next

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        middle.next = self.reverseList(middle.next)

        while dummy:
            temp = dummy.next
            dummy.next = middle.next
            middle.next = temp

            dummy = dummy.next
