1. Share questions you would ask to help understand the question:
- Can nodes have negative numbers?
- Are there at least two nodes in each input?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)

3. Write out in plain English what you want to do: 
- Finding the answer on paper, it is pretty easy, and one common thing that I found with the answers, is that the LCA is always within the range of p and q
    - for example, for p: 2, q: 8, 6 is within the range [2,8]
    - another example, for p: 2, q: 4, 2 is within the range [2,4]
- So, starting from the root, I can traverse down subtrees based on if the current root is > or < than the range. 
    - This means subtress that are outside the range do not get traversed

4. Translate each sub-problem into pseudocode:
- maxNum = max(p, q)
- minNum = min(p, q)
- while root.val not > maxNum and root.val not < minNum 
    - if root.val > maxNum:
        - root = root.left
    - else:
        - root = root.right
- return root

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        maxNum = max(p.val, q.val)
        minNum = min(p.val, q.val)

        while not(root.val <= maxNum and root.val >= minNum):
            if root.val > maxNum:
                root = root.left
            else:
                root = root.right
        return root -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm uses the features of a BST to only traverse nodes that contain the subtree of the potential LCA
- One weak area is that I did use max and min. I could have also done without it by reworking my while conditional to integrate that logic into it. 