1. Share questions you would ask to help understand the question:
- For clarification, "the number of nodes in the given tree is at most 1000" refers to the input correct? Not the disjointed trees?
- Can to_delete be 0?
- Do have to edit the tree itself? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- HashTable (Likely)
- DFS (Likely)
  
3. Write out in plain English what you want to do: 
- What can be done is by using DFS to go through the tree.
- If the current node is in the list of to be deleted node, then that node has to be converted to a null and if it's children exist, they must be roots
- Otherwise, return the node 
- Do this recurisvely for each node and return the output

4. Translate each sub-problem into pseudocode:
- Initialize an output list that will hold all the roots
- Create a helper function that will perform only take in a node: root
    - if the root doesn't exist:
        - return None
    - set root.left equal to dfs(root.left) this will ????????
    - set root.right equal to dfs(root.right)
    - if root.val is in the delete list:
        - check if root.left exists:
            - append root.left to the output list
        - check if root.right exists:
            - append root.right to the output list    
        - return None, effectively delelting the node
    - else:
        - return the root 
    - return the root
- check if dfs(root):
    - append the root to output
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        output: List[TreeNode] = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val in to_delete:
                if root.left:
                    output.append(root.left)
                if root.right:
                    output.append(root.right)
                return None
            else:
                return root
            return root
                
        if dfs(root):
            output.append(root)
            
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the alogrithm only has to traverse through the tree once to both remove the right nodes and append all roots 
    - This works by recursively checking if the nodes exist and then appending if they exist and their parent is to be deleted. 
- Also, there is no additional data structure other than the needed output list
- One weak area is that since I am using DFS, the recursion stack can get massive if the constraint on the number of nodes were larger
- There is also something I wanted to mention, which was a really cool approach that some people took to solve this problem: by using a flag, and going through the Tree and appending from top -> bottom. 