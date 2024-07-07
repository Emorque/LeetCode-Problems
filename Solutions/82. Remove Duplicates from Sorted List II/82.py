from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head 

        p1 = temp
        p2 = temp.next

        while p2:
            if not p2.next or p2.val != p2.next.val:
                p1.next = p2
                p1 = p1.next
                p2 = p2.next
            else:
                p3 = p2.next
                while p2.val == p3.val:
                    if not p3.next: 
                        p2 = p3.next
                        p1.next = p2
                        return temp.next 
                    p3 = p3.next
                p2 = p3
        return temp.next