class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None
        
        p1 = slow

        while p1.next:
            if p1 == head:
                return p1
            p1 = p1.next
            head = head.next 