1. Share questions you would ask to help understand the question:
- Should I return 0 if there is there are no nodes in the tree?
- Will there be any trees where multiple nodes are at the same minimum depth

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- Breadth-First-Search (Likely)
  
3. Write out in plain English what you want to do: 
- So this problem is pretty similar to the maxDepth problem. The difference is that since we only need the min, I can just take the logic from that problem and apply it here with min instead of max. Additionally, I would need to add two more conditionals for the chidren. This is because if there is a node that only has one child, once the algorithm explores the other child, it would be as if that node is a leaf. 

4. Translate each sub-problem into pseudocode:
- have a base case if the root doesn't exist: return 0
- check if there is a left child:
    - if not, return and call the minDepth funcation on the right child + 1
- check if there is a right child:
    - if not, return and call the minDepth funcation on the left child + 1
- now, nodes that pass those conditionals have to have both children and exist, so return min(minDepth(left + 1, minDepth(right + 1))

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One weak area is that since I am using a BFS algorithm, I could have used a DFS algorithm with queue for improve runtime. 
- One strong area is that the algorithm 