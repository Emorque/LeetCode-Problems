1. Share questions you would ask to help understand the question:
- Does this mean that there will be at least 2 int in nums?
- Do the partitions have to be of equal length?
- What are the ranges that an int can be? Negative/0?
- Do the partitions have to be consecutive?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP (Likely)

3. Write out in plain English what you want to do: 
- With a decision tree made, just with 4 numbers, the amount of calls made got expensive, but I realized that there are some repeat calculations. For example, I would see [2,8] and [8,2], subsets, which are different but they have the same sum. 
- I think that is where I can afford to make some kind of optimization. Instead of checking every possible subset in a dfs, what if I store the sums that I currently have in a cache?
  - Seemingly at each following number, I just take the sums that I currently have and then just add my current number to them
- Eventually, if I can reach my target, then I can immediately return True.
- Also, since the subsets are equal, meaning together they are 2y, then the sum of all of the numbers in nums has to be even. If it isn't then I know no matter what, no equal subsets are found, so I can return false right away
  - And as for target, it would be y
- In terms fo containing these sums, instead of appending to a list, using a set would make it easier to avoid having duplicate sums, which would just grow my data list larger compared to a set; if I am adding my current number to all of the numbers that I have currently stored

4. Translate each sub-problem into pseudocode:
- Get the sum of the nums List
- If it is odd, return False 

- set target = sum // 2
- initialize a sums set

- for num in nums:
  - for sum in sums:
    - newSum = sum + num
    - if newSum == target:
      - return True
    - if newSum > target:
      - continue
    - sums.add(newSum)

- if all sums were calculated and target was never found, return False

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False
        
        target = total // 2
        sums = set()
        sums.add(0) #ensures the current num gets added to sums

        for num in nums:
            if num == target:
                return True
            newSums = set()
            for currSum in sums:
                newSum = currSum + num
                newSums.add(currSum)
                if newSum == target:
                    return True
                if newSum > target:
                    continue
                newSums.add(newSum)
                
            sums = newSums

        return False -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, thanks to using two sets (I realized you cannot iterate through a set while it is being edited), I have a collection of all potential sums which are used in placed of their subsets. 
- One weak area is that it may not be clear why using these two sets works, which some comments explaining the reasoning and going through a case, it may be more clear