from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        dummyA, dummyB = headA, headB

        while dummyA is not dummyB:
            dummyA = dummyA.next if dummyA else headB
            dummyB = dummyB.next if dummyB else headA

        return dummyA
