# from collections import deque

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        h = ListNode()
        h.next = head
        p1 = h  

        while True:
            p2 = p1
            for i in range(k):
                if not p2.next:
                    return h.next  
                p2 = p2.next

            prev, curr = None, p1.next
            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            temp = p1.next  
            p1.next = prev  
            temp.next = curr  

            p1 = temp