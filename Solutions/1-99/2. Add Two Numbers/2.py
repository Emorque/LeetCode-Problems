from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        current = answer
        carry = 0

        while l1 or l2 or carry:
            addition = carry
            if l1:
                addition += l1.val 
                l1 = l1.next
            if l2:
                addition += l2.val
                l2 = l2.next
            current.next = ListNode(addition % 10)
            current = current.next
            carry = addition // 10
        return answer.next