1. Share questions you would ask to help understand the question:
- What is the range that x and y can be?
- What is the range that points can be in terms of length?
- Are the points distinct?
- Is the points array sorted in any way?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Min spanning Tree -> Prims's Algorithm
  - Minheap with a set of visited nodes and an adjacency list

3. Write out in plain English what you want to do: 
- This problem does seem difficult, and the big thing that I am thinking of, is trying out, prim's algorithm

- For this to work, I would need an adjanceny list, and instead of only storing the adjacent nodes to the current node's list, I also want the manhttan distance there as well, so it can be referenced later

- Then comes using prim's algorithm

- Intiailize a visited set, so that when a node is connected to the end graph, it is no longer considered for a min cost
- Initialize a minheap with the starting value: [0,0] (cost,point), so that the first point can be grabbed and of course, the cost to itself is 0. This (cost,point) is also what is in the adjacency list
- Intiialize an output int

- while the visited set < the number of points: (once this is no longer true, it means all points are connected and no more connections are needed)
  - cost, point = heapq.heapop(minHeap)
  - if the point is in the visited set, continue since it it already connected to the graph
  - when this is no longer true, then the current cost obtained is the min cost/closest point to the current node
  - add the cost to the final output int
  - Now that the point is "added" to the final graph, add the point to the visited set

  - for each adjcent point that the current point has:
    - if that point is not in the visited set, meaning that this is a potential edge to form:
      - push the [cost, adjacent point] to the minHeap

- return the output int

4. Translate each sub-problem into pseudocode:


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numPoints = len(points)

        adj = { i:[] for i in range(numPoints)} #Initializes each point(index) with an empty adjacent list 
        
        for i in range(numPoints):
            x1, y1 = points[i]
            for j in range(i + 1, numPoints):
                x2, y2 = points[j]
                manhattan = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([manhattan, j])
                adj[j].append([manhattan, i])


        output = 0
        visited = set()
        heap = [[0,0]]
        while len(visited) < numPoints:
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            output += cost
            visited.add(point)

            for aCost, aPoint in adj[point]:
                if aPoint not in visited:
                    heapq.heappush(heap, [aCost, aPoint])
        
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that an adj list, minheap, and set are all used to get the min cost for each node, with the minHeap keeping the min costs in order, set ensuring that points are not revaluated, and the adj list holding the costs of each point with every other point
- One weak area is that there can be a big optimization made, where the code that has the adj list constructued, can be incorporated into the while loop with Prim's algorithm