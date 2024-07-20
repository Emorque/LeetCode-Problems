1. Share questions you would ask to help understand the question:
- Are all the node values unique, including the one to be added?
- For empty trees, is an acceptable output just the desired node?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- BFS (Neutral)

3. Write out in plain English what you want to do: 
- What I am thinking of is to first set up a temp node that is set to the root of the tree and traverses the tree based on the input val
- It will continue to traverse with the input val until it says a None node. Once it does, create a node with the input val and set it to that None node
- Return the root

4. Translate each sub-problem into pseudocode:
- Initialize a temp node that is equal to the root of the tree
- Create a while loop that iterates through the tree while the temp node exists
    - if val <= temp.val:
        - if temp.left doesn't exist
            - set the left child to a new node with the value of val
        - else:
            - set temp to temp.left
    - else:
        - if temp.left doesn't exist
            - set the right child to a new node with the value of val
            - return the root
        - else:
            - set temp to temp.right
            - return the root
- if nothing is returned yet, return a new TreeNode with the value of val

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root

        while temp:
            if val <= temp.val:
                if not temp.left:
                    temp.left = TreeNode(val)
                    return root
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = TreeNode(val)
                    return root
                else:
                    temp = temp.right
        return TreeNode(val) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the alogrithm just needs can traverse the tree and input the new treeNode all in one pass
- One weak area is that the code is a bit lengthly due to being an iterative algorithm.
    - This solution went over my head, some people made use of the existing function insertIntoBST and made a solution where you just recursively call this function. 