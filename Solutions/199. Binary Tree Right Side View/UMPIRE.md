1. Share questions you would ask to help understand the question:
- Can the tree be empty?
- Do we neccesarily care about the values that are in the tree? Since we only care about their positioning

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Likely)


3. Write out in plain English what you want to do: 
- What this looks like to me, is that the question whats the post-traversal of the BT, until the most bottom right node is reached
  - Once that happens, just return the current List
- For the sake of practicing BFS, I'll try with this algorithm, only appending right children

4. Translate each sub-problem into pseudocode:
- Initailize a queue with the root as an element, and an output list 
- While the queue has content:
  - pop from the queue 
  - append the val from the queue to list 
  - append the right child only of the currNode back to the queue
- return the output list


- Nevermind, there is a testcase: [1,2], where the answer is [1,2]

- If a left child is present when a right child isn't, than that left child is the right most view. So, what this tells me is that BFS can be used traditionally, appending all of the nodes at the current level. However, those nodes get popped until the rightmost node is found. That node is then what get appended to the output List

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        nodeCount = 1
        currCount = 0

        if not root: return output

        queue = [root]

        while queue:
            for i in range(nodeCount):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    currCount += 1
                if node.right:
                    queue.append(node.right)
                    currCount += 1
            output.append(node.val)
            nodeCount = currCount
            currCount = 0

        return output  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that constant ints are used to keep track of the number of nodes per level, and the logic of BFS is used for a more readable algorithm 
- One weak area is that it could have been simplier if I used something like len(queue) for my for loop