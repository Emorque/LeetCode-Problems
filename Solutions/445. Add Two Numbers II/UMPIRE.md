1. Share 2 questions you would ask to help understand the question:
- Can this be done without reversing the LLs?
- Is it possible that the resulting LL has more nodes than the input LLs?
  - ex: L1 and L2 have 4 nodes, and the result LL has 5 nodes

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two Pointers (Likely)
- Multiple Passes (Likely)

3. Write out in plain English what you want to do:
- Unlike Add Two Numbers I, the numbers here are not reversed. 
- Something then, that can be done is iterating through the LLs, with each iteration, appending the current Node's value to a stack. 
- Then once we have the stack, we iterate through them, keeping track of the carry, and then creating new nodes with the sum and setting them to a temp Node
- We would then return the head of LL

4. Translate each sub-problem into pseudocode:
- Iterate through each LL, with each iteration, appending the current value into their respective stack. 
- Set a while loop: (while stack1 or stack2 or carry)
  - calc the values for stack1 and stack2:
    - 0 if empty, .pop() if not
  - Set the sum equal to values of stack1.pop and stack.pop and carry
  - Create a new temp node with the value of the sum % 10
  - Set a carry with the value of sum // 10
  - to have it so that we are constantly setting a new head:
    - set the temp node's .next -> head
    - set head = temp node
5. Translate the pseudocode into Python and share your final answer:
  <!--
  class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();

        while (l1 != null){
            stack1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null){
            stack2.push(l2.val);
            l2 = l2.next;
        }

        int carry = 0;
        ListNode head = null;

        while (!stack1.isEmpty() || !stack2.isEmpty() || carry != 0){
            int val1 = stack1.isEmpty() ? 0 : stack1.pop();
            int val2 = stack2.isEmpty() ? 0 : stack2.pop(); 

            int sum = val1 + val2 + carry;
            
            ListNode temp = new ListNode(sum % 10);
            carry = sum / 10;
            temp.next = head;
            head = temp;
        }
        return head;
    }
}
  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it utilizes the correct data structures that intuitively reverses the LLs
- One weak area is that I realized while doing the problem, this could be done through not using the stack data structure. Seeing CodePath's solution confirmed this as there is a way to recusively create a call stack by creating a helper function that calls itself recursively as it is iterating through the LLs. What is cool about this is that since this is a call stack, the first execution will always be on the rightmost digit and then go from right -> left. 