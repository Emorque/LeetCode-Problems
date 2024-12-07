1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- First, I definetly need a new array answer that is of length n to match temperatures
- So I should be able to do this in one pass
- I just need a way to track previous temps, so that warmer temps can be applied to all previous colder temps 
- So after trying an example, a stack will be extremely useful. It will hold all temps that currently don't have a next warmer day
- Then when I do come across a warmer day, I can continually check the stack to see if my current temp is warmer than the temp in the stack
- Once it isnt, all other temps in the stack should be warmer than my current temp so no need to worry
- The thing is that I do need to calculate the difference in days between the temps to put in the answer array, so I think appending indexes to the stack would be better. Then I could just get the temp by checking the temperatures array at the index

4. Assess the space/time complexity:
- Space: O(n) where n represents the number of temps in temperatures. If every day doesn't have a warmer day after it (decending order), then the indexes stack will have all n temps
- Time: O(n) as all temps need to be processed

5. Optional - Give any ways you would improve your solution: