1. Share questions you would ask to help understand the question:
- Will the values of the arrays be unique?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Divide and Conquer (Likely)

3. Write out in plain English what you want to do: 
- The first thing that jumped out to me, was that for any preorder array, the first element is always the root of that tree
- Another thing, is how inorder works (left, self, right); this means that when looking at the node in an inorder array, the nodes that are to the left belong to it's left subtree, and the same for the right

- Using these two ideas, a divide and conquer algorithm can be used to break these arrays down for each node when they are created
- The same buildTree function can be recursively called to build the current node's left and right subtrees

4. Translate each sub-problem into pseudocode:
- if len(preOrder) == 0:
  - return None (this array has no nodes)

- set root to a ListNode(preOrder[0])

- for i in range(len(inorder)):
  if inorder[i] == root.val:
    break

- root.left = buildTree(preOrder[1 : i + 1], inorder[0 : i])
- root.right = buildTree(preOrder[i + 1:], inorder[i + 1:])


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break

        root.left = self.buildTree(preorder[1: i + 1], inorder[0: i])
        root.right = self.buildTree(preorder[i + 1:], inorder[1 + i:])

        return root  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it uses the traversals of pre and inorder to break down the algorithm into one digestible solution that can be repeated
- One weak area is that this will get really slow, wherea as using a more effective method like index() and a queue would make my algorithm run faster