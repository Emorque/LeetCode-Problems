1. Share questions you would ask to help understand the question:
- Are the nodes in the tree all unique values?
- Will nodes p and q point to different nodes?
- Are nodes p and q guarenteed to exist in the tree?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Recursion (Likely)

3. Write out in plain English what you want to do: 
- All we care about are the two nodes that we desire, p and q, and the node that is their LCA
- So an algorithm can be set up recursively with the function I already have: lowestCommonAncestor
- A base case is set up to return itself when the root does not exist, or if it is a match for p or q 
- If that is not the case, the children need to be processed first in a post-order traversal 
- Recursively call lowestCommonAncestor on the left and right children 
- Now, the two calls will return either None or the node that matches p or q 
- If the current node has both left and right returning a node, than the current node has to be the LCA. 
- If this is not true, there are now three other potential cases. 
    - Both left and right return None
    - Only left returns a node
    - Only right returns a node
- In this case, only the subtree that has a node needs to be carried over. So, an or statement can be used to return only left or right if they exist 

4. Translate each sub-problem into pseudocode:
- Set up a basecase that returns the current root when it doesn't exist or it equals p or q
- Call lowestCommonAncestor on the left child 
- Call lowestCommonAncestor on the right child
- If left and right:
    - return root 
- return left if left else right 

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm only needs to traverse through the tree once to obtain the LCA
- One weak area is that the algorithm is that it gets more inefficient if the input tree is unbalanced  