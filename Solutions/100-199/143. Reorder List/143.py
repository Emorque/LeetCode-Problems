from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        #stack
        tails = []
        tail = mid
        while tail:
            tails.append(tail)
            tail = tail.next

        tempHead = head
        while mid.next and tails:
            tail = tails.pop()
            tailNext = tempHead.next

            tempHead.next = tail
            tail.next = tailNext

            tempHead = tailNext
            tails[-1].next = None

        return head
