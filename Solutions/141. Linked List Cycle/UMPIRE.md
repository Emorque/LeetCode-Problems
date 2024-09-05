1. Share questions you would ask to help understand the question:
- Can there be an empty LL?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointer 

3. Write out in plain English what you want to do: 
- There is one key thing that makes a LL cycle, and that is that there is no None after a tail
- So, while iterating through the LL, if a Null Node is ever reached, than for sure, the LL is not a cycle and False can be returned
- So, to know that a cycle exists, two pointers moving at different speeds will be needed 
- If they move at the same speed, than the function will never end if the LL is a cycle
- If the two pointers intersect, than that means that faster pointer had to have looped around and then caught up to the slower pointer, True can be returned  

4. Translate each sub-problem into pseudocode:
- Intiialize two pointers at the head
- while fast:
    - fast = fast.next.next
    - slow = slow.next
    - if fast == slow:
        - return True
- return False

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that only 2 pointers are used, which helps save memory space
- One weak area is some comments can be added to make the reasoning behind the code clears