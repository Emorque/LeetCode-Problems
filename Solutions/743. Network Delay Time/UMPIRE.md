1. Share questions you would ask to help understand the question:
- Can nodes point to more than one node?
- Are there duplicate elements in times?
- What are the ranges for the time values? 
- If a node is connected to multiple nodes, does the signal travel to every connected node at the same time?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Djistkras

3. Write out in plain English what you want to do: 
- Breaking down this problem further, a simipler question would be to ask, what is the mimimum time to reach node x from the starting node?
  - Once I know the answer for the starting node's neighbors, I can then go to those neighbors and ask the same question
    - I will do this until every node is visited
    - And another thing is that to be able to store the mimimum time, using a minHeap will be immensly useful

- So this is like doing BFS, except with a priority queue (minHeap) instead of a regular queue

4. Translate each sub-problem into pseudocode:
- Create an adjacency list where the key is the node itself, and the value is a list of (node the current node points to, time to reach it)
- Intialize a time int

- create a minHeap with the starting value: [(0, k)] time, node because minHeap sorts based on this first index
- create a set so that once a node's min path time is found, no need to calculate it again
- create a while loop that iterates so long as the minHeap has content. I thought of doing it based on the length of the set matching n nodes, but since there are cases where it may not be possibe for all nodes to get the signal, this condition will cover that (if a set length is used on a failed test, there will be an error where I'd be popping from an empty minHeap)
  - pop from the heap
  - if node is in set:
    - continue
  - set.add(node)
  - time = time from pop, setting this and not adding because we want the min time to each node, not the sum of mins

  - iterate through the current node's neighbors:
  - for node, ntime in adj[poppednode]:
    -  if node not in set:
      - heappush([ntime + time from pop, node]) to minheap. Summerize both times so that the minTime is carried till the end

return time if len(set) == n else return -1

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            pTime, pNode = heapq.heappop(minHeap)
            if pNode in visited:
                continue
            visited.add(pNode)
            time = pTime

            for node, nTime in adj[pNode]:
                if node not in visited:
                    heapq.heappush(minHeap, (nTime + pTime, node))
        
        return time if len(visited) == n else -1
         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm uses a bfs approach with a priority queue (minHeap) instead of regular queue, so that I am traversing down the paths that have a min time
- One weak area is that this solution is not the most clear