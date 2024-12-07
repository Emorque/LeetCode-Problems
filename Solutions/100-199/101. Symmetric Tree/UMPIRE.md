1. Share questions you would ask to help understand the question:
- Do the nodes have unique values?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- DFS (Likely)
- BFS (Neutral)

3. Write out in plain English what you want to do: 
- This problem reminds me of the invertTree problem, so while the answer will be different, the logic of setting left to right and right to left could be used here
- Set up a helper function that will take in two nodes, left and right 
- check if both values are equal and recursively check if the left's left is equal to right's.right and that right's left is equal to left's right 
- I guess what I am saying is that on the left subtree, we traverse all the left nodes to compare with all the right's subtree right nodes and vice versa
- return the result 

4. Translate each sub-problem into pseudocode:
- create a helper function that will take in two nodes: left and right:
    - if left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left):
        - return True
    else:
        - return False
    - for a base case, if either or reach a null node, then that means traversal is complete
    - if not left and not right:
        - return True
    - if there is a case where it is not symetrical in terms of the nodes itself, like when when left reaches a node and right doesnt:
    - if not left or not right:
        - return False
- return helper(root, root)


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True 
            if not left or not right:
                return False
            if left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left):
                return True
        return helper(root, root)
         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm traverses through the tree differently for the left and right to match what a mirrored tree looks right: left's left should match the right's right, and the left's right should match the right's left 
- One weak area is that this is a recursion approach which could get memory inefficient. Using an iterative approach could redudce the likelihood of this happening, perhaps with a stack?