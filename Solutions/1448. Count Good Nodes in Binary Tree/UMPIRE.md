1. Share questions you would ask to help understand the question:
- For every test case with at least one node, is the top root always a good node?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- BFS (Neutral)

3. Write out in plain English what you want to do: 
- By going over the examples, what defines a good node seems to be that the node's val is greater than or equal to the maximum value in the current path to it. 
- So if a root is 3, but the left child is 1. When that left child gets analyzed, its value is less than the maximm value in it's path (3), so it won't count as a maximum good node
- Since these paths should be considered independently, I think DFS would be a better approach 

- A helper function can be made, where it has the parametes, node and maxValue
  - If the node's val is greater than or equal to the maxValue, increment the output val by 1. 
  - If it has children, recursively call the helper on its children with the updated maxValue 

4. Translate each sub-problem into pseudocode:
- intialize an output int with an value of 0 
- def DFS(node, maxValue):
  - nonlocal output
  - if node.val >= maxValue:
    - output += 1
  - maxValue = max(maxValue, node.val)
  - if node.left:
    - DFS(node.left, maxValue)
  - if node.right:
    - DFS(root.right, maxValue)

- DFS(root, root.val)
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0 

        def DFS(node, maxValue):
            nonlocal output
            if node.val >= maxValue:
                output += 1
            maxValue = max(maxValue, node.val)
            if node.left:
                DFS(node.left, maxValue)
            if node.right:
                DFS(node.right, maxValue)
        
        DFS(root, root.val)
        return output  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that DFS and a constant int is used to keep track of the current path's maxValue to quickly check viability
- One weak area is that since DFS is used, the space complexity is depended on the node of numbers, since every node gets processed seperately 