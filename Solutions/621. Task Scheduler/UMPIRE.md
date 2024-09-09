1. Share questions you would ask to help understand the question:
- Can n by 0?
- Is there guarenteed to be at least one task in the list?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Heap (Likely)
- Hashmap (Likely)

3. Write out in plain English what you want to do: 
- one easy test case to solve, is that when n == 0, every task can be done right after the other, no matter if they are equal. So, the len of tasks can be returned in this case 
- There are some things that first need to be realized:
    - n can also be the interval. So, if n is equal to 2, a space of 3 characters (n + 1) must be filled before used characters can be repeated again. 
    - the tasks list is not sorted, so something like a hashmap can be used to obtain the frequencies 
    - a heap can then be used to keep the most frequent characters on top
    - another data structure, like a stack (something with quick insert/deletion) to hold characters that were used
    - and since the tasks are only characters 'A' - 'Z', each structure can have at most 26 length 

4. Translate each sub-problem into pseudocode:
- if n == 0:
    - return len(tasks)
- Intialize a hashmap, stack, and list to later be heapified, and output int 

- for task in taksks:
    - update task frequency in hashmap 

- for key, value in hashmap:
    - heappush value, key into heap 

- interval = 0 
- while heap or stack 
    - if !heap and !stack:
        - output += interval
        - return output
    - if !heap:
        - append stack items back to heap
        - output += n + 1
        - interval = 0
    - pop from heap 
    - push popped character to stack 
    - interval += 1
    - if interval == n + 1:
        - append stack items back to heap 
        - output += interval
        - interval = 0
- return output
        

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        charFreq = {}
        charSeen = []
        chars = []
        output = 0

        for task in tasks:
            charFreq[task] = 1 + charFreq.get(task, 0)

        for key, value in charFreq.items():
            heapq.heappush(chars, (value * -1, key))
        
        interval = 0
        while chars or charSeen:
            if not chars:
                while charSeen:
                    heapq.heappush(chars, charSeen.pop())
                output += n + 1
                interval = 0
            freq = heapq.heappop(chars)
            if freq[0] != -1:
                charSeen.append((freq[0] + 1, freq[1]))
            interval += 1
            if interval == n + 1:
                while charSeen:
                    heapq.heappush(chars, charSeen.pop())
                output += interval
                interval = 0
                
        return output + interval  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a heap is used to sort the character frequencies from most freqeuent, so that they are considered first in an interval.
- One weak area is that this solution requires 3 data structures, which even though that are most O(26) space, may not be the most ideal 