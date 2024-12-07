1. Share questions you would ask to help understand the question:
- Is there intervals array in any sorted order (ascending/decensding)?
- Is there guarenteed to be at least one interval 
- Can starts/ends be negative?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Sorting (Likely)

3. Write out in plain English what you want to do: 
- I think a useful way to visualize this problem is with a number line, where each interval represents an interval/section of that number line. 
- Then, going from left to right on that number line, see if there are any overlapping intervals, which would only be when the end of one the current interval is greater than or equal to the start of the next interval 
- If this isn't the case, then the current interval is not overlapping with anything
- Using these two rules, a current interval can be tracked, adjusted, and appended to an output list depending on if it is overlapping with another interval

4. Translate each sub-problem into pseudocode:
- Initialize an output list
- Sort the intervals array by the start numbers 
- set currInterval to the first interval in the list, the constraints say that there is always at least one 
- set a for loop that intervals from index 1 to the end of the intervals list 
  - if currInterval[1] >= intervals[i][0]:
    - currInterval[1] = max(currInterval[1], intervals[i][1])
  - else:
    - append the currInterval to the output list
    - set currInterval to interval[i]
- append once more the currInterval to output
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key=lambda x: x[0])

        currInterval = intervals[0]

        for i in range(1, len(intervals)):
            if currInterval[1] >= intervals[i][0]:
                currInterval[1] = max(currInterval[1], intervals[i][1])
            else:
                output.append(currInterval)
                currInterval = intervals[i]
        output.append(currInterval)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that only one traversal of the intervals is needed after sorting to building upon intervals. 
- One weak area is that sorting is needed for this algorithm to work, since it relies on the starting values of each interval to be in ascending order. 