1. Share 2 questions you would ask to help understand the question:
  -  What should we do if the kth value exceeds the length of the list?
  -  In a similar vain, what about empty lists or null?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
  - Heap: Likely
  - Linked List: Unlikely
  - Stack: Unlikely

3. Write out in plain English what you want to do:
  - First, we create the class, kthLargestElement
  - For Kth largest element, we would:
    - Create a min-heap with the input nums
    - Since we only want the kth largest element (in terms of sorted)
      - We would continually pop the heap until we have at most k number of elements
  - For add, we would:
    - Add the new element into the heap
    - Then pop once more so that the root of the heap is still the kth largest
    - Lastly, return the root with peek

4. Translate each sub-problem into pseudocode:
- class kthLargestElement:
  - initialize the heap and k with the given values
  - heapify nums
  
- add:
  - push the new val into the heap
  - have a while loop that iterates for as long as there are k elements
    - pop from the heap
  - we now have a heap of size k meaning that return the [0] of the heap is the kth largest element 

5. Translate the pseudocode into Python and share your final answer:
  <!--    
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while (len(self.heap) > self.k):
            heapq.heappop(self.heap)

        return self.heap[0] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
  - Strength: it uses the restriction of only caring about the kth largest to its advantage by discarding the elements less then it and making the kth largest always the root

  - Weakness: there could be a check in add that checks if the newly added val is less than the root of the heap. If that is the case, then there is no need to heappush and then heappop, since we would just be adding that val, only to then remove it. 