1. Share questions you would ask to help understand the question:
- How are the cities labeled? 0 - (n -1)
- Is it possible for a two cities to have flights that go to each other (doubly directed)?
- Can I assume that all the flights in flights list are unique?
- What range can I expected prices to be?
- What is the range I can expect the number of flights to be?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS, minHeap, Set (Likely)

3. Write out in plain English what you want to do: 
- Adjacency List with the city as a key, and the value being a list of (cost, destination city)
- minHeap to sort these flights so that the ones with the smallest cost are popped first
- visited set so that already processed cities don't get processed again 

- On second thought, using something like a minHeap wouldn't be the most ideal, since what if going down the min route doesn't make it to the src node in k stops, but a more costly route does?
- In that case, a solution without it can be done
- First, creating two seperate lists for the number of nodes I have. 
- One will be what holds the current min distance to each node, and the other will be what gets edited and then set to the first list after editing
  - For the second list, when comparing min prices, since I am adjusting the prices of this list, I want to use the list that was set before any edits are made (so the first list)

4. Translate each sub-problem into pseudocode:
- Intiailize an orginial list of length n with every value as the max price possible + 1
- set original[src] = 0

- while k != -1
  - set a deep copy of the original list
  - iterate through the flights in flight:
    - if copy[src] + price < original[dst]:
      - original[dst] = copy[src] + price
  - k -= 1

- return originial[dst] if changed, else return -1

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        original = [float("inf")] * n   
        original[src] = 0

        while k != -1:
            copy = original.copy()
            for fro, to, price in flights:
                if copy[fro] + price < original[to]:
                    original[to] = copy[fro] + price
            k -= 1
        
        return original[dst] if original[dst] != float("inf") else -1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm builds upon a previous price list so that when adjusting min values, I change min values only compared to the list when there were no changes at this stop step
- One weak area is that this solution does do duplicate work but itereating through the flights list k+1 times. My original idea of a BFS + minHeap and set was too greedy to work, so I'd be interested to see if there are ways to do this with one pass of flights