1. Share questions you would ask to help understand the question:
- Can this be thought of as a next step to the max depth question?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Pre-Order (Likely)

3. Write out in plain English what you want to do: 
- What should be done is recursively check the height of each node
- This can be done in a similar vein to the maximum depth question, where as the algorithm traverses down nodes, it as 1 to some count to then be placed in a max
- With the height obtained, then it comes time to calculate the diameter
- This can be done by also using a max method to pass the max of the current diameter vs the sum of the left and right subtrees

4. Translate each sub-problem into pseudocode:
- Initialize a diameter variable to be the output 
- Create a helper function that will take in a node: root and return an int
    - if the root does not exist:
        - return 0
    - left = helper(root.left)
    - right = helper(root.right)
    - diameter = max(left+ right, diameter)
    - return max(root.left + 1, root.right + 1)
- call helper on root
- return diameter

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 

        def helper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            nonlocal diameter
            diameter = max(diameter, left + right)
    
            return max(left + 1, right + 1)
        helper(root)

        return diameter -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm is able to complete the problem by only traversing through the tree once
- One weak area is that, as with other solutions like it, it is recursive. In this case, the max number of nodes is 10^4, but if it were larger and the test cases were unbalanced trees, memory use could get out of hand. 