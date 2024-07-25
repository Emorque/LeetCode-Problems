1. Share questions you would ask to help understand the question:
- Will there be any empty tress?
- Are the values in the nodes all distinct?
- Are nodes guaranteed to have either 0 or 2 children?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Recursion (Likely)


3. Write out in plain English what you want to do: 
- What can work here is using InOrder traversal, since for a valid bst, InOrder traversal should always be in ascending order 
- Therefore with inorder traversal and by always checking the previous value to ensure that it is in ascending order, I can verify that the tree is valid or not
- This can be done with a helper function that appends nodes InOrder and compares the current node with the top of a stack 
    - This stack gets poped everytime to avoid unneccessary data holding and adds the current node before moving onto the next one
    - Only until the tree is no longer valid, that the output can be set to false and then pushed as an answer

4. Translate each sub-problem into pseudocode:
- Initialize a stack that holds negative infinity
- Initalize an output with True 
- Create a helper function that only takes in a node: root:
    - if the root doesn't exist or the output is False:
        - return (No need to keep traversing once the tree is no longer valid)
    - call helper on root.left
    - check if root.val <= stack.pop():
        - if this is true: set output to false
    - append root.val to the stack
    - call helper on root.right 
- call helper on the root
- return the output


6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack : List[int] = []
        # stack.append(-math.inf)
        stack.append(-2**31 - 1)

        output = True
        def helper(root: Optional[TreeNode]):
            nonlocal output
            if not root or not output:
                return
            helper(root.left)
            if root.val <= stack.pop():
                output = False
            stack.append(root.val)

            helper(root.right)
        helper(root)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the tree only needs to be traversed once and the stack never grows larger than needed, since in InOrder traversal, only the current and last node need to be considered
- One weak area is that this algorithm is using an extra data structure, with a stack, even if it doesn't get very large
    - There are actually some creative solutions that avoid this, and instead and a range (min and max parameters) in their helper functions to determine if the node is within that range and return the result. This helps with space complexity. 