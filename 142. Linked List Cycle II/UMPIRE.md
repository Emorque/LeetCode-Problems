1. Share questions you would ask to help understand the question:
- Can math can be used to determine the start of the cycle?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointers (Likely)
- Sliding Window (Unlikely)
- Multiple Passes (Neutral)
  
3. Write out in plain English what you want to do: 
- This be seems to be the question: Linked List Cycle with one extra step. 
- Therefore, we can just steal the code from the that question: having two pointers going at different speeds to determine if the LL is a cycle
- Then, if the LL is confirmed to be a cycle, we can go further.
- The location where the two pointers meet in the first part can be considered our Intersection point. 
- The distance the slow pointer traveled is from H (Head) + D (Distance from H to Intersection)
- The distance the slow pointer traveled is from H (Head) + D (Distance from H to Intersection), all times 2 since it travels every 2 nodes per step
- Therefore, we have the equation 2H + 2D = H + D + L (length of the cycle)
- Simplifies to H + D = L
- Changes to H + D = N * L (N is the number of times the cycle has been traversed)
- Simplies to H = NL - D
- This means that to find the entry of the cycle
- Move H and Intersection by one node each iteration, the entry being when they intersect

4. Translate each sub-problem into pseudocode:
- Initialize two pointers on the head. 
- Have a while loop that interates so long as pointer fast and fast.next are not null:
    - have slow move ones and fast move twice
    - if they match, break from the loop
- if fast or fast.next are null, then return None

- Initialize another pointer, this time, on the slow/fast pointer 
- while p1.next is not null:
    - if p1 is equal to head, return p1
    - move p1 and head by one

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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
            head = head.next  -->



6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this is done in constant memory, as only pointers are used
- One weak area is that less pointers could be used and perhaps a helper function could have been used