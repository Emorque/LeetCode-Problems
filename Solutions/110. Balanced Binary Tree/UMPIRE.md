1. Share questions you would ask to help understand the question:
- So basically means that the difference in depth of any nodes cannot exceed 1 correct?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- Helper (Likely)

3. Write out in plain English what you want to do: 
- I can set up a similar solution to the maxdepth problem
- Except I just return a unique number, -1 whenever there is a difference between the two child nodes that is greater than 1

4. Translate each sub-problem into pseudocode:
- Set up a helper function that takes in a node and returns an int
    - If the node doesn't exist, return 0
    - set leftHeight to helper(leftChild)
    - set rightHeight to helper(rightChild)
    - if the either heights are equal to -1,
        - return -1
    - if the abs(leftHeight - rightHeight) > 1:
        - return -1
    - return the max height between leftHeight + 1 and rightHeight + 1
- call helper on root and set to result
- return if result == -1

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(currNode: Optional[TreeNode]) -> int:
            if not currNode:
                return 0
            
            leftHeight = helper(currNode.left)
            rightHeight= helper(currNode.right)

            if (leftHeight == -1 or rightHeight == -1):
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight + 1, rightHeight + 1)
        result = helper(root)
        return result >= 0 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that if there is ever a time when two nodes are greater than 1 in terms on height difference, that -1 carries for future recursive calls
- One weak area is that the if conditionals could have been simplified and called after each time helper is used