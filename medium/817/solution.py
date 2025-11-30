from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res = 0
        dummy = head

        while dummy:
            if dummy.val in nums:
                while dummy and dummy.val in nums:
                    dummy = dummy.next
                res += 1
            else:
                dummy = dummy.next

        return res
