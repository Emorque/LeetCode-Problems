1. Share questions you would ask to help understand the question:
- Is there a possible test case where the LL is all duplicates?
- To add to that, what about cases where there are back-to-back duplicates: 1 -> 1 -> 2 -> 2 -> ...

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Multiple Pointers (Likely)
- Sliding window (Likely)
  
3. Write out in plain English what you want to do: 
- What we want to do is essentially slice off an group of duplicates in the LL 
- How this can be done is by starting from left to right, recognizing the group of duplicates and marking with a pointer the end of the group. Then we go from the node before the start and set it's 'next' value to the node after the end. 

4. Translate each sub-problem into pseudocode:
- Since theres a chance that the head of the LL is a duplicate, we should use a temp node to point to the head
- We start with pointer p1 pointing to temp, with p2 pointing to p1.next
- while p1.next 
    - if p2 is equal to p2.next:
        - create a pointer p3 that points to p2.next
        - create a while loop that continues until p2 != p3
            - if p3.next == null, have p2 = p3.next and break
            - have p3 equal p3.next
        - set p2 = p3 and p3 = p3.next
    - Now, since p2 and p3 are no longer equal, set p1.next equal to p2
    - 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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
        return temp.next-->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm traverses through the LL once and is able to return the answer
- One weak area is the amount of conditionals. To improve this, I would definetly, rework the conditionals so that at the very least, I don't have an if nested in a while, nested in an if. 