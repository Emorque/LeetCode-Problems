1. Share questions you would ask to help understand the question:
- Is the nums array sorted?
- Does nums have at least 1 int?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Tracking? (Likely)

3. Write out in plain English what you want to do: 
- Right now, what I am having trouble thinking of something other that a more brute force solution
  - That what be where I have a for loop that iterates through the nums list
    - Then I'd have an inner for loop that tracks a currentSum from index i in the outer to the end of the nums list
      - at every instance, I would track the max to. 
- With this brute force solution, every possible subarray to considered, but since it houses two nested for loops, it is not the most time effcient 

- By not doing it the brute force way, I think an O(n) solution can work by using two ints, one to track the maxSum, and one to track the currSum
- the logic goes that a current Sum is tracked unitl a number is found to be greater than the current Sum. When that happens, the left nums can just be dropped, since they'll never be apart of the maxSum as a whole
- Also, a maxSum is calculated at each step, so as not to forget the maxSum that has already been found 

4. Translate each sub-problem into pseudocode:
- Initailize currSum, maxSum to nums[0], since there is at least one interval
- for i in range(1, len(nums)):
  - if the current num is >then currSum (AND currSum < 0):
    - set currSum to the current num
  - else:
    - add current Num to currSum 
  - set maxSum to max(maxSum, currSum)
- return maxSum

- One thing I forgot, I only considered that the left side of nums would be deterimental, but what if there was a case like [1,2]
- There needs to be another check:  
  - if currNum is a positive number, it can help with getting the maxSum, so it should be added.
  - if currNum is a negtaive number, then it'll only hurt the current Number, so set currNum to the current number

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > currSum and currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area about this algorithm is that it is done in O(n) time, by using constants to track important sums (2 ints), which is vastly more efficient that the brute force approach I mentioned first
- One weak area is that I could add some comments, to explain why each part of that if statement matters. 