1. Share questions you would ask to help understand the question:
- So basially, every test case has a graph with some cycle in it?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- 

3. Write out in plain English what you want to do: 
- Something we can is have a parent data strucutre that starts with each node being its own parent
- Then, when two nodes are connected, they then are made to have the same parent
- If an edge occurs between two nodes that share the same parent, return that edge, as by adding this edge, we turn this graph into a cycle

4. Translate each sub-problem into pseudocode:
- parents list, size list 
- for i in range(0, len(edges) + 1)
  - parents.append(i)
  - size.append(1)

- def getParent(n):
  - p = parents[n]
  - while p != parents[p]:
    - p = parents[n]
  - return p 

- def setParent(n1, n2):
  - p1, p2 = getParent(n1), getParent(n2)

  - if p1 == p2:
    - return False

  - size1, size2 = size[p1], size[p2]

  - if size1 > size2:
    - parents[p2] = parents[p1]
    - size[p1] += size[p2]
  - else:
    - parents[p1] = parents[p2]
    - size[p2] += size[p1]

  - return True

- iterate through the edges list 
- if not setParent: return edge

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents, size = [], []

        for i in range(len(edges) + 1):
            parents.append(i)
            size.append(1)
        
        def getParent(n):
            p = parents[n]
            while p != parents[p]:
                p = parents[p]
            return p
        
        def setParents(n1, n2):
            p1, p2 = getParent(n1), getParent(n2)

            if p1 == p2:
                return False
            
            size1, size2 = size[p1], size[p2]

            if size1 > size2:
                parents[p2] = parents[p1]
                size[p2] += size[p1]
            else:
                parents[p1] = parents[p2]
                size[p1] += size[p2]

            return True
        
        for a, b in edges:
            if not setParents(a, b):
                return [a,b]
                 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area with this algorithm is that by using the parents and sizes lists, I can always know what the current parent of a node is, and the sizes helps with making sure that parents are always set if we get [a,b] or [b,a]
- One weak area is that it is not the more clear without the diagram that I drew. Having a test case written along with this can make navigating what is going on more clear. 