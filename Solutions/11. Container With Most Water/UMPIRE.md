1. Share questions you would ask to help understand the question:
- Can there be a test case where we have two really tall lines, followed by a ton of smaller lines that result in an higher output?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointer (Likely)
- Sliding Window (Neutral)
  
3. Write out in plain English what you want to do: 
- Something we can do is set two pointers, one at each end of the array. 
- Then we calculuate the area between the two pointers and set it to the result if it is greater than the current max.
- Then depending on which pointer is lower, adjust the placement of the pointers 
- Just do this until the pointers intersect and return the result 

4. Translate each sub-problem into pseudocode:
- Set two pointers, the left one at 0 and the right one at len(height) - 1
- Set an int variable: result to 0 
- while the left pointer is less than the right:
    - calculate the distance between them and multiply it by the shorter height of the two. This is area
    - set result to max(result, area)
    - whichever pointer points to the shorter height, have it move once 
- return the result 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            width = right - left
            if height[left] < height[right]:
                area = width * height[left]
                left += 1
            else:
                area = width * height[right]
                right -= 1
            result = max(result, area)
        return result -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that there is no need for multiple passes, we just shrink the area as we calculate the areas
- One weak area is that there is greater potential for it to be much faster. There are some creative solutions that use open()