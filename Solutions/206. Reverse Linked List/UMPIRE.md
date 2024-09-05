1. Share questions you would ask to help understand the question:
- Can the LL be empty?
- Can the LL be a cycle?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointer

3. Write out in plain English what you want to do: 
- So, to reverse the LL, I need to first consider the strucutre of a LL
- A LL starts from a head node, and points to a next node, until it reaches the last node, which itself points to a NULL next node
- So, to reverse, I should start with a NULL node, and then, set it's next node to the head
- Then, iterating through the LL, take each node and set its next value to the previous node
- Once a null value is hit, return the curr node

4. Translate each sub-problem into pseudocode:
- initialize a None node and set it's next to the head
- set a traverse Node to the head, this will be what traverses 
- set a currNode to the None node created at the start
- while temp != None:
    - prev = currNode
    - temp = temp.next
    - currNode = temp
    - currNode.next = prev
- return currNode

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = None

        while head:
            prev = currNode
            currNode = head
            head = head.next
            currNode.next = prev
        return currNode  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this is an iterative solution, meaning that no memory is used for a recursion stack
- One weak area is that there is three pointers used, all meant to keep track of nodes, since adjusting .next values would mess with instances of currNode.next, and head.next; which can be hard to follow