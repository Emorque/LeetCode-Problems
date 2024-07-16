1. Share questions you would ask to help understand the question:
- Will all trees will be valid?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- Iterative (Likely)
  
3. Write out in plain English what you want to do: 
- What I can do is set up a helper function that will recursively traverse through the tree in inorder
- Then append those nodes to an outer list

4. Translate each sub-problem into pseudocode:
- Initialize a list that will hold the nodes' values
- Set up a helper function that takes in a node
    - if the node doesnt exist:
        return
    append the node value to the list
    call helper(node.left)
    call helper(node.right)

5. Translate the pseudocode into Python and share your final answer:
  <!--  class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def helper(root: Optional[TreeNode]):
            if not root:
                return
            helper(root.left)
            output.append(root.val)
            helper(root.right)
        
        helper(root)
        return output
        -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm is very easy to visualize. 
- One weak area is that this algorithm is done recursively. An iterative solution would be an intersting challenge, since the in-order values need to be returned. 