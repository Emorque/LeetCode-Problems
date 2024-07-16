1. Share questions you would ask to help understand the question:
- Is it viable to search through the tree twice, to find the start and dest nodes?


2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- Breadth-First Search(Likely)
- Depth-First-Search(Likely)
  
3. Write out in plain English what you want to do: 
- Thankfully, since the nodes have unique values, there is no need to worry about processing the wrong nodes. 
- Hint 1 gave me the idea to use the Lowest Common Ancestor
- So, first I need to construct a helper function that finds the LCA between the start and dest values
- Once the LCA is obtained, now I need to constuct another helper function that finds the path from the given root to the destNode
    - This should be done in BFS 
- Call this path function twice, with the root being the LCA, and the destNodes being the start and dest values respectively. 
- Manipulate the lists so that they match the traversal path from the start node to the dest Value
- return that result

4. Translate each sub-problem into pseudocode:
- First, set up a helper fuction to get the LCA between the two nodes:
    - Takes in a node, start value, dest value, and returns a node (LCA)
    - if the root doesn't exist or the root is equal to the start/dest values:
        - return the root
    - set left to helper(root.left, start, dest)
    - set right to helper(root.right, start, dest)
    - if both left and right exist, meaning that both nodes where found from opposite subtrees branching from the current root:
        - return root
    - if this doesn't execute, that means that the nodes have to both be in the left subtree or the rightsubtree
    - in that case, return the left subtree if left exists or the right subtree if that exists

- Set up a startPath list
- Set up a destPath list
- Next, set up a helper function that will construct the paths to the start/dest nodes from the LCA
    - Takes in a root, destNode, and a path 
        - if the root doesn't exist:
            - return False
        if the root.value == destNode:
            - return True because the node has been found
        - check the left and then right subtrees:
        - if helper(root.left, dest, path)
            - append 'L' to the path
            - return True
        - if helper(root.right, dest, path)
            - append 'R' to the path
            - return True
        - if neither work, then the destNode is not a descentdent of the current root
        - return False
- Call helper(LCA, startValue, startPath)
- Call helper(LCA, destValue, destPath)

- The path goes from destValue -> root:
    - From 5 -> 2 -> 6. 2 is 5's right child, and 6 is 2's left child
    - The path looks like ['L', 'R']

- The startPath can be transformed to a string consiting of 'U' * len(startPath)
- Then iterating from right to left with the destPath, add the character to Start Path
- Finally, return startPath

5. Translate the pseudocode into Python and share your final answer:
  <!--  class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def LCA(root: Optional[TreeNode], startValue: int, destValue: int) -> Optional[TreeNode]:
            if not root or root.val == startValue or root.val == destValue:
                return root
            left = LCA(root.left, startValue, destValue)
            right = LCA(root.right, startValue, destValue)

            if left and right:
                return root
            return left if left else right

        def helper(root: Optional[TreeNode], destValue: int, path: list):
            if not root:
                return False
            if root.val == destValue:
                return True
            if helper(root.left, destValue, path):
                path+='L'
                return True 
            if helper(root.right, destValue, path):
                path+='R'
                return True   
            return False

        ancestor = LCA(root, startValue, destValue)
        startPath = []
        destPath = []

        helper(ancestor, startValue, startPath)
        helper(ancestor, destValue, destPath)

        startPath = 'U' * len(startPath)
        for i in range(len(destPath) - 1, -1, -1):
            startPath += destPath[i]

        return startPath
        -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- This one was a real challenge
- One strong area is that the algorithm hinges on the idea of a Lowest Common Ancestor. It was such a helpful hint and got the ball rolling. With the LCA, the problem just gets broken up into two more manageable problems
- One weak area is that there are some things that could be made more efficient such as joining the two paths at the end, and making the helper function more readable