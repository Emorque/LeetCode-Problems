1. Share questions you would ask to help understand the question:
- If an intervals end is equal to another interval's start values, are they considered to be overlapping?
- Will there  by at least 1 interval in intervals?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Sorting

3. Write out in plain English what you want to do: 
- By representing the intervals on a number line, I determined that there are two ctest cases that I want to consider:
  - when the current interval's end is greater than the start of the next interval:
    - if this is the case, there is overlapping
    - the current interval's end when needs to change
  - if this doesn't happen, then there is no overlap, so the current interval can be reset to the interval currently being traveresed 

- This works great when the intervals array is sorted by the starting values
- If the interval is not sorted, then it gets difficult to know for sure that already traveresed intervals are not greatly overlapping the number line 

4. Translate each sub-problem into pseudocode:
- sort the intervals array by the start values
- initialize an ouput int to 0 
- initialize a currentInterval list to interals[0], there is guarenteed at least one interval in the array

- Then, set a for loop that iterates from index 1 to the end of the intervals array
  - if the end of the currentInterval is greater than the start of intervals[i]: 
    - there is overlap
    - increment output by 1
    - set currentInterval's end to the minimum between currentInterval's end and the end of intervals[i]
    - this way, the most intrusive interval is "removed"
  - else:
    - there is no overlap, so set currentInterval to intervals[i]

- return output 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        output = 0  
        currInterval = intervals[0]

        for i in range(1, len(intervals)):
            if currInterval[1] > intervals[i][0]:
                output += 1
                currInterval[1] = min(currInterval[1], intervals[i][1])
            else:
                currInterval = intervals[i]
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area with this algorithm is that since the array get sorted, when it comes to removing overlapping intervals, only the one that has the greatest end needs to be "removed", since it'll be the one less likely to overlap with future ascending intervals
- One weak area is that this algorithm will only work if the intervals array is sorted. If it isnt, then it becomes a different problem on how to remember previous intervals to compare when a potential overlap occurs. 