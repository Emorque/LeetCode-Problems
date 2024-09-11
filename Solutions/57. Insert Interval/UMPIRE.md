1. Share questions you would ask to help understand the question:
- Can the new interval be a range that goes beyond what intervals already has?
- Can start or end be negative?
- Can a new interval be added that is already in intervals?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- 

3. Write out in plain English what you want to do: 
- For a new interval to be overlapping with a current interval, the two things cannot be true
    - The start of the new interval is greater than the end of the current interval
    - The end of the new interval is less than the start of the current interval
- If both are not true,
    - Then the new interval and the current interval overlap

- Iterate over the intervals list, and use this logic to adjust the new interval. If there is overlap, adjust the values of new interval

- if the newInterval gets added, break out and enter a new loop to add the remaining intervals to the output list

4. Translate each sub-problem into pseudocode:
- initialize an output list

- for i in range(len(intervals)):
    - if newInterval[0] > intervals[i][1]:
        - output.append(intervals[i])
    - elif newInterval[1] < intervals[i][0]:
        - output.append(newInterval)
        - return output + rest of intervals
    - else:
        - newInterval[0] = min(newInterval[0], intervals[i][0])
        - newInterval[1] = max(newInterval[1], intervals[i][1])
    
- if nothing was returned, the end was reached with newInterval not yet appended:
    - so append newInterval

- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            currInterval = intervals[i]

            if newInterval[0] > currInterval[1]:
                output.append(currInterval)
            elif newInterval[1] < currInterval[0]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], currInterval[0])
                newInterval[1] = max(newInterval[1], currInterval[1])

        output.append(newInterval)
        
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the newInterval list is adjusted to grow in range when it comes across an overlapping interval, allowing for easy comparisons
- One weak area is that I should add some comments explaining why those two if statements work for determining overlap