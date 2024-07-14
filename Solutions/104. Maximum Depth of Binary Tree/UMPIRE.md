1. Share questions you would ask to help understand the question:
- Will there be a test case where there is are only right/left children?
- Should 0 be returned for null cases?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- Level search (Likely)

3. Write out in plain English what you want to do: 
- Since it returns an int, it can be used to our advantage.
- Set a basecase for when the root is empty. And if it isn't, just return the max value of the 

4. Translate each sub-problem into pseudocode:
- Have a base case when the root doesn't exist: return 0
- Else, return the max(maxDepth(leftChild) + 1, maxDepth(rightChild) + 1)

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is the algorithm just goes down each child and increases a count. No extra constraint was needed so no more processing than needed was used
- One weak area is that an iterative solution can be used for cases that require a lot of recursive calls. 