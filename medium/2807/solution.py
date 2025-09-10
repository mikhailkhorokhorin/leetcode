from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def findGreatestCommonDivisor(a: int, b: int):
            while b != 0:
                a, b = b, a % b
            return a

        left_node = head
        while left_node.next:
            right_node = left_node.next
            gcd_node = ListNode(findGreatestCommonDivisor(left_node.val, right_node.val))
            left_node.next = gcd_node
            gcd_node.next = right_node
            left_node = right_node

        return head
