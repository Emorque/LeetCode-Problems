1. Share 2 questions you would ask to help understand the question:
- Will there be test cases in which two seperate consecutive sequences have the same length?
- Can this be done without using a sorting algorithm?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Set (Likely)
- Table (Likely)
  
3. Write out in plain English what you want to do: 
- What we can do is use a set and iterate thorugh that set, only incrementing a counter variable when we encounter consecutive numbers
- We would need to use a max() method to only carry over the longest sequence, because, until we reach the end, we won't know for sure that we have the longest sequence. 

4. Translate each sub-problem into pseudocode:
- Create a set with the elements from nums (tackles cases like example 2)
- Create a longest_sequence counter variable
- for num in numsSet:
    - We check to make sure that the current num minus 1 is not in the set. 
        - This is to prevent needless sequence counting.
            - For example, if we have the sequence [1,2,3,4], we want to enter the loop when we encounter 1. Without this check, we end up calculating the sequences starting at 2, 3, and 4
        - If true, then we check if nums plus 1 is in the set. If so, we set the curr_sequence counter variable to 1
        - set a currNum to num + 1
            - While this is true, increment curr_sequence and currNum by 1 each time
        - Set longest_sequence counter to max(longest_sequence, curr_sequence)
- return longest_sequence

- Previous solution time exceeded
- The following uses .sort()

- Use .sort() to sort the nums List
- Then set the longest_sequence and curr_sequence counters to 1
- for i in range (len(nums)-1):
    - if nums[i] is equal to nums[i+1], use continue to go to i+1
    - if nums[i] + 1 == nums[i+1], increment the curr_sequence counter by 1 
    - else: set longest_sequence counter to max(longest_sequence, curr_sequence) and set curr_sequence back to 1
- return max(longest_sequence, curr_sequence) 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_sequence : int = 1
        curr_sequence : int = 1

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] : continue
            if nums[i] + 1 == nums[i+1]:
                curr_sequence += 1
            else:
                longest_sequence = max(longest_sequence, curr_sequence)
                curr_sequence = 1
        return max(curr_sequence, longest_sequence) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it is very efficient relatively speaking, which I was surprised, I figured set would be more efficient. 
- One weak area (for the set solution), likely has to do with the construction of the set. Because the for loop should be more time efficient than the "sort" solution since checking "in" in set is O(1); which is more efficient than going over the entire list. 