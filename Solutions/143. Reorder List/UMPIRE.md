1. Share questions you would ask to help understand the question:
- Should a LL of one and 2 nodes be returned as the same?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointer

3. Write out in plain English what you want to do: 
- There is an added constraint in that "You may not modify the values in the list's nodes. Only nodes themselves may be changed."
- This means that the next values will need to be adjusted for the relevant nodes
Drawing out the second example, we seem to end once the middle node's next value is none 
  - To get the middle node, a fast pointer (.next.next) and a slow pointer (.next) can be used
  - For odd length LLs, this is middle is found
  - For even length LLs, need to push the slow pointer once more
- set a while loop that iterates so long as middle's next node is not null
  - have a pointer that starts at the head, and then keep track of the that head's next, and the tail. Reorder by setting new next nodes 

4. Translate each sub-problem into pseudocode:
- Initialize a slow and fast pointer and tempHead to head
- 
- while (fast.next.next):
  - slow = slow.next
  - fast = fast.next.next

- if fast.next:
  - fast= fast.next
  - slow = slow.next

- while slow.next:
  - tail = slow
  - while tail.next.next:
    - tail = tail.next
  - newNext = tail
  - newNext = newNext.next
  - oldNext = tempHead.next
  - tempHead.next = newNext
  - newNext.next = oldNext
  - tail.next = None
  - tempHead = tempHead.next

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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
  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm utilizies a stack to keep track of what tails are, my previous solution did not use this. So, when it came to finding the new tail for that instance, a pointer would have to traverse from the slow pointer to the end; which for large LLs, can take a long time
- One weak area is the readability, especially since I am popping twice from the stack and then appending again, it may be hard to follow 