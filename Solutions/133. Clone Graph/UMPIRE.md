1. Share questions you would ask to help understand the question:
- Can return any node in the deep copy graph?
- Is every value unique?
- Can node be empty?
- Are the elements in the list in neighbors type nodes?
- What is the range of the length of neighbors

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- hashmap (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- How I am thinking this will go, is that for each node given, I need to create a deep copy of it, keeping its val and list of neighbors
- Using something like DFS will be very helpful in traversing through the nodes given as when traversring that neighbors list, I can just recursively call dfs on each element in that list
- The tricky part comes in how I can remember the copies that I made, as just calling dfs may just leave it in the void
- A hashmap can work in that the key will be the original node, and the value will be the copy of that node
- That way, once a copy of the node is made, I can easily reference it by looking at the hashmap

4. Translate each sub-problem into pseudocode:
- Initialize a hashmap 
- create a dfs helper function(node)
  - if node in hashmap:
    - return hashmap[node]
  - create a new node with the val of the given node
  - hashmap[node] = clone
  - for neighbor in node.neighbors:
    - clone.neighbor.append(dfs(neighbor))
  - return clone

- return dfs(node)

5. Translate the pseudocode into Python and share your final answer:
<!-- 
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        def dfs(root):
            if root in hashmap:
                return hashmap[root]
            if not root:
                return 
            clone = Node(root.val)
            hashmap[root] = clone

            for neighbor in root.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        return dfs(node) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a hashmap is used to keep track of already made clones so that, when appending neighbors, if a clone is already made, the hashmap will have that relationship so that clone can be returned right away
- One weak area is that it may not be as clear what the dfs is doing in the recursion stack. I should have commented that it is important that hashmap[root] clone comes before the recursion call, since it may seem odd that have that relationship, only to then keep building clone's neighbor list
  - It is so that that relationship can be reference in the recursive calls