from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        dummy = head
        while dummy:
            res.append(dummy.val)
            dummy = dummy.next

        return res == res[::-1]
