1. Share questions you would ask to help understand the question:
- Can there be duplicate points in the array?
- What should be done if there are points that have the same distance?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Heaps (Likely)

3. Write out in plain English what you want to do: 
- Using a bit of math, this problem can be solved using the pythagorean theorem, since the points are just being measured to the distance
- And, since the goal is to find "K closest points", a heap can be used to get a sorted list
- So, by combining the two logic, the end result can be a list that gets the first k points of the heap

4. Translate each sub-problem into pseudocode:
- intiailize a list to be heapified, and an output list of length k 
- for each x, y in points:
    - distance = sqrt(x ** 2 +y ** 2) 
    - heappush(distance, (x, y))

- for i in range(k)
    output[i] = heappop[1]

- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        output = [0] * k

        for x,y in points:
            distance = sqrt(x ** 2 + y ** 2)                
            heapq.heappush(heap, (distance, (x,y)))

        for i in range(k):
            output[i] = heapq.heappop(heap)[1]
            
        return output  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm uses a heap to handle the sorting of closest points for us
- One weak area is that there cna be some improvements. 
    - popping from the heap while inserting whenever the heap's length is > k. Farther points are no longer needed
    - sqrt isn't really needed, something like abs() can work fine, since the sqrt of a smaller number if smaller than the sqrt of a larger number