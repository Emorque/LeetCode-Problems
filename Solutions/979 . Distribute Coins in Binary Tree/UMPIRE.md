1. Share questions you would ask to help understand the question:
- Can there ever be more coins than nods?
- Can there be less coins available than nodes?
- Can coins be pushed to nodes that already has coins?


2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Recursions (Likely)


3. Write out in plain English what you want to do: 
- For this problem, there are two questions that need to be answered at each node: 
    - how many coins can I give to my parent?
    - how many moves are processed between my child nodes?
- To solve these two questions, the child nodes need to be processed first, which means the solution would need to use post-order traversal 
- For the first question, this can be calculated by getting the coins from the current node + the left subtree + the right subtree - 1 since 1 needs to be kept at the current node
- For the second question, the moves can be processed by the sum of the absolute values of the left and right subtress 
    - For example, if the left child has 0 coins, and the right child has 2 coins, and the left has 0, two moves are processed: right -> parent; parent -> left
- So, a helper function can be set up to perform this logic in DFS
- A global moves variable should be inialized and incremented whenever the second question is answered at each node 

4. Translate each sub-problem into pseudocode:
- Initialize a moves variable to hold the output
- Create a helper function that just takes in a node: root
    - if the root doesn't exist:
        - return 0 
    - call helper on the left child
    - call helper on the right child

    - calculate the number of coins that are available to the parent: root.val + left + right - 1
    - calculate the moves that need to be processed: abs(left) + abs(right)
        - the reason for abs is because there is a change the node is 0, so when doing 0 + 0 + 0 - 1, it would return -1, meaning it needs a coin, rather than saying I can give a coin
        - this need for a coin needs to recognized as a move
        - increment the moves variable by this
    - return the number of coins avialable to the parent
- Call the helper function on the root
- return moves 

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves: int = 0
        def helper(root: Optional[TreeNode]) -> int:
            nonlocal moves

            if not root:
                return 0 
            left = helper(root.left)
            right = helper(root.right)

            moves += abs(left) + abs(right)

            return root.val + left + right - 1
            
        helper(root)
        return moves -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm only needs to traverse through the tree once 
- One weak area is that the it could be made more readable with comments and type annotations 