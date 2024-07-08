1. Share questions you would ask to help understand the question:
- Do we care if folder are named the same?
- Will there be a test case where it is just comprised of "../" and/or "./"
- Can a folder be named ".d1/"?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)
- Recursion (Likely)
  
3. Write out in plain English what you want to do: 
- Since we are dealing with a directory, a data structure that can be used is a stack
- However, since we don't need to remember the folders themselves, we can use the idea of a stack through an int variable
- Sepending of the strings we see as we iterate through the logs list, we either add or subtract from the level variable
- Then, return the value of level 

4. Translate each sub-problem into pseudocode:
- Initialize count variable : level
- Iterate through the values in logs with a for loop:
    - if the string matches "x/", count++ 
    - else if "../",
        - if level > 0:
            count-- 
    - don't need to check the other condition './' since we'd just remain in place
- Then return level

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0

        for log in logs:
            if (log[0] != '.'):
                level += 1
            elif (log == "../"): 
                if level > 0:
                    level -= 1
        return level -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that we are using the idea of a stack but not using the memory of time of one, since we only care about the level of directories we are in. 
- One weak area is that it may not be as clear as if we were to use a stack. Using a stack may be easier to visualize and would have to the used if we needed to remember any data. 