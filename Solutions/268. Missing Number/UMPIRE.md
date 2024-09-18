1. Share questions you would ask to help understand the question:
- What is the expected range of length of nums:
- Is the nums array sorted?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Sorting (Likely)
- Hashmap (Likely) / Second list
- Math (Likely)

3. Write out in plain English what you want to do: 
- There are three solutions that I came up with that each have their own unqiue constraints:
  - Sorting -> Requires O(nlogn) time to sort and would require n time to traverse through nums 
  - Hashmap -> Requires O(n) space, and would have to pass nums once and the hashmap once (2n) time
  - Math -> I know there is some math problem that gives the expression: n + n - 1 + n - 2... 0, but I dont know it by heart. If I were to use this, then I just compare the sum of nums to what my sum would be with that expression. The difference between the two is the missing number
    - The problem is that if n is large, like 10000, then the expression returns 10000 + 9999 + 9998...0 which may produce an overflow
  - So instead of using that formula to get the sum right away:
    - I know that the sum of nums and the sum of n has a difference of the missing number
  - So, what I can do is iterate through nums, subtracting the current num from my output, and then adding the current index
    - What this does, is bascially subtract the sum of nums one at a time, and add the sum of n one at a time
      - No overflow will happen, and the resulting int will be the difference between the two, since just one number differs between the two
  - Basically, for [1,2]:
    - I would:

4. Translate each sub-problem into pseudocode:
  - missing = 0
  - for i in range(len(nums)):
    - missing += i
    - missing -= nums[i]
  - returning missing + i + 1

  - 0 + 0 - 1 = -1
  - -1 + 1 - 2 = -2

  - -2 + 1 + 1 = 0

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0

        for i in range(len(nums)):
            missing += i
            missing -= nums[i]
        
        return missing + i + 1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that instead of using a formula to getting one potentially breking sum, I am adding and subtracting parts of the two sums, one small integer at a time
- One weak area is that it may not be clear why that return is like that 