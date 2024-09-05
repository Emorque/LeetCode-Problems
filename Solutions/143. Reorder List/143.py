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
        slow, fast, tempHead = head, head, head
        
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                break

        stack = []
        stackLength = len(stack)
        tails = slow
        while tails:
            stack.append(tails)
            tails = tails.next

        while slow.next:
            # tail = slow
            # while tail.next.next:
            #     tail = tail.next
            newNext = stack.pop()
            tail = stack.pop()

            oldNext = tempHead.next
            tempHead.next = newNext
            newNext.next = oldNext
            tail.next = None
            
            stack.append(tail)
            tempHead = tempHead.next.next
