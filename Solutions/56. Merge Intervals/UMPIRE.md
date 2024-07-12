1. Share questions you would ask to help understand the question:
- Are I allowed to use a sorting method? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Sliding Window (Likely)
- Two Pointer (Likely)

3. Write out in plain English what you want to do: 
- What I can do is have the intervals List sorted by the first numbers in the inner list.
- Then I can interate through the list, checking for overlapping lists intervals and only appending a completed interval to my result whenever there is no longer any overlapping 
- Repeat this for until I reach the end of the intervals list 

4. Translate each sub-problem into pseudocode:
- Initialize a result list and sort the intervals list by the start of each interval
- Set up a loop that interates through each interval in intervals
- if the result list is empty or if the current interval's start is more than the previous interval's start:
    - append the current interval
- else:
    - set the result's list rightmost interval's end to the max value between the current interval's end and the result's list rightmost interval's end
- return the result

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if len(result) == 0 or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, aside from sort, the algorithim only needs to run through the intervals list once 
- One weak area is that I am using a sort and max. Perhaps a better by using comparions like <, >, ==