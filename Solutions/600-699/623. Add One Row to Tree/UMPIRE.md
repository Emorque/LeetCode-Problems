1. Share questions you would ask to help understand the question:
- Can the structure of the inital left and right subtrees be maintained?
- Do the values itself serve another purpose? Besides being what is in the row that gets pushed?
- Can the new depth be at the very bottom?
- Are all the values unique?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS(Likely)
- BFS(Likely)

3. Write out in plain English what you want to do:
- This can be broken down into smaller problems
- First, traverse through the tree until depth-1 via DFS
- Second, for all nodes in that depth, store their left and right child as temps, even if null
    - Then, set their left and right child nodes to new nodes with the value val
    - Go to the left newly created child, and set its left subtree to be that stored left child from before
    - Go to the right newly created child, and set its right subtree to be that stored right child from before
- Return back the root of the tree

4. Translate each sub-problem into pseudocode:
- Has the base case for when the depth is 1:
    - Create a new Node, with the value val, and set its left child to be the root
    - Return the new node
- Create a dfs helper function that will traverse through the tree until the depth-1 is hit
    - if the current depth is equal to depth-1:
        - set a temp left node to the current node's left subtree
        - set a temp right node to the current node's right subtree
        - set current node's left child to a new node with the value val
        - set current node's right child to a new node with the value val
        - set that left child's left subtree to the temp left node
        - set that right child's right subtree to the temp right node
    - else:
        - dfs(root.left, dep + 1)
        - dfs(root.right, dep + 1)
- set a rootTemp node to root        
- Call dfs with (rootTemp, 1)
- return root

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        def dfs(node: Optional[TreeNode], dep: int):
            if not node:
                return
            if dep == depth-1:
                tempLeft = node.left
                tempRight = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = tempLeft
                node.right.right = tempRight
            else:
                dfs(node.left, dep+1)
                dfs(node.right, dep+1)
        dfs(root, 1)
        return root
         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm only traverses to the depth that is most needed, which is depth-1. So if there is a really deep tree but the given depth is relatively small, there is no need to traverse the rest of the tree
- One weak area is that dfs is used, which is a bit less efficient than using BFS, so a more efficient solution would use BFS. 