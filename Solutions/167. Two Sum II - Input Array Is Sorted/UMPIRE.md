1. Share questions you would ask to help understand the question:
- Can there be negative numbers in the array?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash map (Neutral)
- Two pointers (Likely)

3. Write out in plain English what you want to do: 
- If the array was not sorted, then a hashmap could be used during traversal to find the answer
- However, since the array is sorted, and I'm limited to constant space, two pointers can be used
- Have one pointer at the start and one at the end. Add the values the two pointers point to, and if they equal the target, return it
    - If the sum is greater, then we need to take away; and since this array is in ascending order, moving the right pointer left will do this
    - If the sum is less, then the same logic applies, we need more and going to the right with the left pointer does this
    - Sort of like a tightrope, depending on the sum, we evenly distribute the weight by taking away/adding balance (in this case, int values)
- Keep that loop going, since there is always a solution

4. Translate each sub-problem into pseudocode:
- Initialzie two pointers, one at the start and one at the end
- Create a while loop that iterates until the two connect, 
    - if the sum of the values are equal to the target, return the indexes
    - if the sum is less than the target, increment the left pointer
    - else: decrement the right pointer 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1

        while p1 < p2:
            currSum = numbers[p1] + numbers[p2]
            if currSum == target:
                return [p1 + 1, p2 + 1]
            elif currSum < target:
                p1 += 1
            else: 
                p2 -= 1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area with this algorithm is that it uses constant extra space, with only 3 int variables
- One weak area is that it could be made more clear the reasoning why this logic was followed, through the use of comments