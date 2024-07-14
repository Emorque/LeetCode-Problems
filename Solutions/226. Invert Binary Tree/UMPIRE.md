1. Share questions you would ask to help understand the question:
- Will there be a case to switch places between an existing node and a non-existing one?
- Will two nodes that swap every have the same value?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- HashMap (Unlikely)
  
3. Write out in plain English what you want to do: 
- So what I can do is, as we traverse through the binary tree, swap the nodes of the left and right children. Keep doing this until the bottom of the tree is reaches (no more children)


4. Translate each sub-problem into pseudocode:
- Set up a base case where the node doesn't exist: return
- Have the left child equal to invertTree(rightChild) and vice versa
- return the root 

5. Translate the pseudocode into Python and share your final answer:
  <!--class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return 

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm just swaps the child nodes themselves. No extra constraint was needed so no more processing than needed was used
- It is a relatively simple solution, so one weak area is that if there is a really deep tree as a test case, using an iterative solution with queue could improve efficiency 