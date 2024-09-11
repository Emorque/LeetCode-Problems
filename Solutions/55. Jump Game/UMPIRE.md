1. Share questions you would ask to help understand the question:
- If we only care about the reaching the last index, does that mean that we don't really care what value is at the last index?
- Can there be negative values? Would the person we forced to go back?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Tracking? (Likely)

3. Write out in plain English what you want to do: 
- A brute force solution would be to do something like dfs, where at your current, recursively check all possible jumps and see if it can reach the end. A jump can be determined True if its values is greater than or equal to the distance from it to the end

- After some time, I think this can actually be done in one pass O(n), by using some conditionals and keeping track of jump distance
- The logic goes:
  - if nums[i] is greater than the current tracked jump length, then set jump to nums[i]. If we stop here, we can go further.
  - else:
    - if nums[i] is equal or less, than we are still going at our max potential jump, no need to consider this nums[i]
    - since some distance was traveled, do jump - 1
  - if jump is ever less than 0, meaning we reached some a spot we can't possible reach, return False

4. Translate each sub-problem into pseudocode:
- initialize jump int to 0
- create a for loop that traverses through num in nums:
  - if jump < 0:
    - we over exereted, so return false
  - if num > jump:
    - set jump to num
  - else:
    -jump -= 1
- there may be a case were we have overexerted and reached the end with a -1.
- so in that case, return (jump >= 0)
  - if jump is 0, we just barely made the jump to the last index
  - if jump is greater, we had a lot more leeway
  - if jump is less, we just barely missed the last index

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 1

        for num in nums:
            jump -= 1
            if jump < 0:
                return False
            if num > jump:
                jump = num
        return jump >= 0 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area of this algorithm is that it does one pass of nums, meaning that the time complexity is O(n), and can end even earlier for some test cases
- One weak area is that I did write the logic for why these two if statements make sense, but I never showed it as a comment. A third-party may be confused by a jump int is needed and why the reinitialization of it happens.