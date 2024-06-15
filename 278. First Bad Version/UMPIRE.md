1. Share 2 questions you would ask to help understand the question:
- Can this be done with only 1 API call per iteration?
- What if there is no bad version?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Pointers (Likely)
- Sliding Window (Unlikely)
  
3. Write out in plain English what you want to do:
- This is almost identical to our binary search problem previously
- The only difference is that we know after the first bad version, all following numbers are bad
- This means that once isBadVersion() returns true, we just set high to mid. Once the two poiters pass each other or are equal, return the low pointer. 

4. Translate each sub-problem into pseudocode:
- Set low to 1 and high as n (following the restrictions of the problem)
- While the low and high 'pointers' have not crossed each other or are equal
  - Calculate the mid number between low and high
  - Check if the current mid is bad
    - If yes, then set high to mid
    - If not, then set low to mid + 1 (would be infinite otherwise)
  - Once the two pointers are equal to other, we know that any versions previous are all Good, so we just return low or high. 

6. Translate the pseudocode into Python and share your final answer:
  <!--
  def firstBadVersion(n: int) -> int:
  low = 1
  high = n

  while low < high:
      mid = (low + high) // 2
      if isBadVersion(mid):
          high = mid
      else:
          low = mid + 1 
  return low
  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that for every iteration, we only do an API call once
- One weak area is that, there could be less iterations, at the costs of more API calls