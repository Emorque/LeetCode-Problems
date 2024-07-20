 1. Share questions you would ask to help understand the question:
- Is the target guarenteed to be in the tree?
- Are the values unique?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- BFS (Likely)
- HashMap / HashTable (Likely)

3. Write out in plain English what you want to do: 
- My plan is to recreat the relationships between the nodes into a hashtable through DFS.
- Once recreated, I'll create a sepereate helper function that will iterate through the hashTable to navigate through the nodes while decrementing its current distance value
  - Once that distance hits 0, append the current node's value to the output list
- Return the output list

4. Translate each sub-problem into pseudocode:
- Initialize an output list, hashTable: nodes, and a list for visited nodes
- Create a helper function that takes in a 2 nodes: value, parent:
    - if the root doesn't exist:
        - return
    - set nodes[root.val] = [helper(root.left, root.val), helper(root.right, root.val), parent]
    - return root.val
- call helper(root, None) since the root has no parent

- Create a traverse function that takes in two numbers: value, distance
    - if value is None or the value is in the visited list:
        - return
    - if distance == 0:
        - append the value to the output list
    - else:
        - append value to visited
        - call traverse(nodes[value][0], distance - 1)
        - call traverse(nodes[value][1], distance - 1)    
        - call traverse(nodes[value][2], distance - 1)
- Call traverse(target.val, distance)
- return the output list

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        nodes = {}
        output = []
        visited = []

        def helper(root, parent):
            if not root:
                return None
            nodes[root.val] = [None, None, parent]
            nodes[root.val][0] = helper(root.left, root.val)
            nodes[root.val][1] = helper(root.right, root.val)
            return root.val
        
        helper(root, None)

        def traverse(value, distance):
            if value == None or value in visited:
                return 
            if distance == 0:
                output.append(value)
            else:
                visited.append(value)
                traverse(nodes[value][0], distance-1)
                traverse(nodes[value][1], distance-1)
                traverse(nodes[value][2], distance-1)
        traverse(target.val,k)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that by recreating the tree into a table of relationships, the algorithm is able to create parent relationship that does not exist in the original tree
- One weak area is that the part of the algorithm where the hashTable is created could be simplified to only include the relationship between parent and node. Doing so would both simiplify the helper function and reduce the size of the individual elements in the table
    - And the logic of the second part of the alogrithm would stay the same, with very minor adjustments