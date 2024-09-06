1. Share questions you would ask to help understand the question:
- Can the root and subroot inputs be the exact same tree?
- Will there be a case where the root is actually a substree of the subRoot?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Recursion (Likely)

3. Write out in plain English what you want to do: 
- There two steps that I see where False can be given.
- First, if the subRoot's root node is not in the root tree at all. 
    - If that's the case, return False right away
- Second, the subRoot's root node is somewhere in the root tree, but there is a mismatch between the trees, maybe between values or nodes existing where nodes don't in the other
- If neither of these happen, return True

4. Translate each sub-problem into pseudocode:
- while root.val != subRoot.val:
    - if not root:
        - return False
    - if root.val > subRoot.val:
        - root = root.left
    - else:
        - root = root.right

- def DFS(root, subTreeroot)
    - if not root and subTreeroot or root and not substreeRoot: 
        - return False
    - if root.val != subTreeRoot.val:
        - return False
    - if not root and not subTreeRoot:
        - return True
    - return DFS(root.left, subTreeRoot.left) and DFS(root.right, subTreeRoot.right)

- return DFS(root, subTreeRoot)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def DFS(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return DFS(root.left, subRoot.left) and DFS(root.right, subRoot.right)
            return False


        queue = [root]
        while queue:
            node = queue.pop(0)
            if DFS(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution utilizes BFS and DFS to traverse through the root tree and check if the trees match respectively
- One weak area is that this took some revisions. My original solution was going off the idea that the this was a BST and that there were unique values. Both of which are questions I should have asked. After realizing that, I realized another solution would be to traverse through the root tree with BFS to not lose track of root, and uses a DFS helper function to check matching trees. Mainly for test cases like [1,1], [1]