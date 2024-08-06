1. Share questions you would ask to help understand the question:
- Can there be cases where no vertex are conencted at all?
- Is the source vertex guarenteed to be the "ui" vertex on the list?
    - ex: if the source vertex is 4, will there be one entry in edges that looks like: [4, vi]

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Lilkely)
- BFS (Likely)

3. Write out in plain English what you want to do:
- What I want to do, is to create a map structure, where the keys are represented by the vertexes, and the values are all the vertexes that are adjacent to it.
- The edges list will be iterated, and for each iteration, this map will be populated
- Once completed, iterate from the source vertex, and perform dfs traversal, using a set so that vistied vertexes are not computed again 
- If the destination vertex is found, return true
- If not, return False

4. Translate each sub-problem into pseudocode:
- Initialize a map 
- create a loop that iterates through the edges list:
    - check if ui and vi are in the map
    - if not, create their entries with the opposing vertex as a value
    - if they are, append the opposing vertex to their entry
- initialize a set for the visited vertexes
- create a helper function that performs dfs:
    - add the current int to the set
    - taking the current int, if it matches desination, return true
    - for all in the vertexes in that int's entry in the map, call dfs on them
- return false 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        vertexes = {}
        for u, v in edges:
            if u not in vertexes:
                vertexes[u] = [v]
            else:
                vertexes[u].append(v)
            if v not in vertexes:
                vertexes[v] = [u]
            else:
                vertexes[v].append(u)

        visited = set()

        def helper(vertex: int):
            if vertex in visited or destination in visited:
                return
            visited.add(vertex)
            for dest in vertexes[vertex]:
                helper(dest)
                
        helper(source)
        return destination in visited -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it creates an adjacency matrix of to edges list to simulate a graph
- One weak area is that DFS is perhaps the weakest traversal here. BFS does not have the overhead of the recursion stack, and union find seems to be the fastest. I had not learned about union find before, but does look like a really cool way to find paths of graph vertexes. I will definetly try to learn more about this. 