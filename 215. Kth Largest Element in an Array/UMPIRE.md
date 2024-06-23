1. Share 2 questions you would ask to help understand the question:
- Can this be done using an external data structure?
- What if k is larger than the number of elements? ex: k = 10 when nums only of size 6

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Set (Unlikely)
- Two Pointer (Unlikely)
- Heap (Likely)
  
3. Write out in plain English what you want to do: 
- There are some things that prevent the use of other data structures / processes and explain why a heap would be best
  - Set: We are looking for the kth largest, not caring about the kth largest distinct, so we do can about duplicates
  - Two pointer: Since the array is not sorted, two pointers and other pointer-like solutions do not help

  - Heap: Heaps work because it can sort the list and when deciding to find the kth largest, we can just pop the root until we find the kth largest.

4. Translate each sub-problem into pseudocode:
- We want to heapify the list.
  - However, since heapify ordering from smallest to largest, we just have to use the negative values of each element in nums 
- We then pop the root of the heap k-1 times
- We then return the root of the heap times -1 to reverse the inital negations we did

5. Translate the pseudocode into Python and share your final answer:
  <!-- def findKthLargest(nums: List[int], k: int) -> int:
  numsSort = [-num for num in nums]

  heapq.heapify(numsSort)

  for i in range(k-1):
      heapq.heappop(numsSort)

  return numsSort[0] * -1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strength area is that the algorithm utilizes the benefits of heap to its advantage with its time complexity
- One weak area is that this does require another data structure to hold the negated values of nums. A solution could be done without needing 'numsSort'