1. Share questions you would ask to help understand the question:
- What should be returned for empty trees?
- Can additional data structures be used?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Breadth-First Search (Likely)
- Depth-First Search (Neutral)

3. Write out in plain English what you want to do: 
- Since the desired output is level order traversal, what can be done is to use BFS with a queue
- A queue will be passed through so long as there are values in it, which will first be the root of the root
- While in this loop, the leftmost element from the queue is popped and processed
    - It's values gets added to a list for the current level and its children get added to the queue
- Repeat this loop until all the nodes have been processed and return that final list 

4. Translate each sub-problem into pseudocode:
- Initialize an output list
- Initialize a queue with its value set to the root of the tree
- Create a while loop that iterates so long as the queue is not empty
    - Initialize a currLevel list which will hold all the nodes that the current level
    - Create a for loop that iterates based on the size of len of the queue
        - pop the queue from the left and assign it to a node variable
        - append its value to the currLevel list
        - append the left child to the queue if it exists
        - append the right child to the queue if it exists
    - append the currLevel list to the output list
- Return the output list

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output: List[List[int]] = []
        queue = []

        if not root:
            return output

        queue.append(root)

        while len(queue) != 0:
            currLevel = []
            for i in range(len(queue)):
                currNode = queue.pop(0)

                currLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            output.append(currLevel)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area of this alogrithm is that it utilizes BFS for traversal, which in the sense of a tree, iterates by the level of the tree which is what is needed for level order traversal
- One weak area is that it could be optimzied a bit futher with the use of a queue instead of a list to use popleft().