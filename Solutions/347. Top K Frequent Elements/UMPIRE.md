1. Share questions you would ask to help understand the question:
- Can k be greater than the number of unique numbers?
- Can some numbers appear the same number of times?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash map (Likely)
- 

3. Write out in plain English what you want to do:
- Breaking this down into smaller problems:
  - First, I  need to track the number of occurances for each number
  - Second, I need to extract only the kth most occurances 
    - Append those numbers to a list and return that list at the end 

4. Translate each sub-problem into pseudocode:
- Initialize a hash map to hold the number and its number of occurances
- Iterate through the given nums list, incrementing the count for each number as it is seen
- Iterate through the now filled hash map, populating a heap with the values and keys
- Itereate through the heap, by popping off the kth elements at the top, and appending them to an output list
- Retutn the output list  


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        occurances = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1

        for key, v in hashmap.items():
            occurances.append((-v,key))
        heapq.heapify(occurances)
        output = []
        while k != 0:
            output.append(heapq.heappop(occurances)[1])
            k-= 1
        return output
         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution utilizes the advantages of a heap to give the occurances in decending order
- One weak area is there are three data structures used and it is a bit difficult to follow along