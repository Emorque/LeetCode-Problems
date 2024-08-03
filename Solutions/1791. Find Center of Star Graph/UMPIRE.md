1. Share questions you would ask to help understand the question:
- Could everyone other node (not the center node) have more than one edge?
- How many total edges to nodes are there?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash Table (Neutral)
- List Index (Likely)

3. Write out in plain English what you want to do: 
- So this is a question to a similar vain to Find the Town Judge. 
- However, knowing what I now know, this question could then be simplied in the same vain 
- In the given star graph, there are n nodes, ranging from 3 to 10^5
    - With the length of the edges list being n - 1
- So, if the star graph has 5 nodes, then there are exactly 4 edges
- This answers my first question, every node not the center will only have one edge
- The center node will have more than one edge
- Also, that center node will appear twice within the first two indexes in edges
- Since the given star graph is valid, there is no need to traverse through the rest of edges
- So, just return the center node that appears twice in the first two indexes in edges

4. Translate each sub-problem into pseudocode:
- Set up four ints(n1, n2, n3, n4), to match the 4 nodes that are in the first two indexes
- If n1 matches with n3 or n4, return n1
- Else, return n2 since it would have to match to n3 or n4

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n1, n2, n3, n4 = edges[0][0], edges[0][1], edges[1][0], edges[1][1]
        return n1 if n1 == n3 or n1 == n4 else n2 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that since only the first two indexes are used, the algorithm does not process unneeded edges
- One weak area is that this solution could be made faster without n1, n2, n3, n4