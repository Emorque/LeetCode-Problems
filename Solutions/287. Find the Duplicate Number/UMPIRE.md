1. Share questions you would ask to help understand the question:
- To clarify, there are no negative elements?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointer (Likely)
- Math (Likely)

3. Write out in plain English what you want to do: 
- Since there is a constraint to keep the extra space constant, that removes the possibility of a set of hashmap 
- Also, the follow-up of linear runtime means that brute forcing the solution of two pointers won't be applicable
- One alternative solution is too use plain old math
- The input array is guarenteed to have elements in the range [1,n]. 
- This means, that the sum of the array can always be found from just knowing n. 
- Therefore, after calculating this sum with math, I can just iterate through nums array, subtracting from the sum. 

- I realized that this math approach does not really for this problem, if just the need for the duplicate to be found is needed, it can work. However, since the duplicate number needs to be returned, this doesn't really work. 
- And then, after realizing that this problem is more of a LL problem in disguise, the solution became more clear. 
  - The indexes and values can be used to emulate a LL. 
  - Using a slow and fast pointer, once they intersect, a cycle is in the LL, and since the input is guareteed to have a duplicate, this will always be true
  - Now, using Floyd's alogrithm, by setting another pointer at the "head" (index 0) of the array, and then setting the pointers to their "next" node, when they intersect, that is the entrance of the cycle. In this case, that also means that duplicate of the array, as it'll be the only num that has two references (appearence at 2 indexes)

4. Translate each sub-problem into pseudocode:
- initialize a slow and fast pointer at 0
- while True:
  - slow = nums[slow] (nums[i] <= n, so 5 will never be in a length 5 array)
  - fast = nums[nums[fast]]
  - if slow == fast:
    - break

- slow = 0 
- while True:
  - slow = nums[slow]
  - fast = nums[fast]
  - if slow == fast:
    - return slow

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this alogrithm fulfills the question and follow-up requirements
- One weak area is that it is not as understandable at a glance. The reason why this works is more clear with a proper LL. With something called Floyd's algorithm, the distance between the initial intersection of slow and fast is always equal to the distance between the start of the cycle and the head. Some comments could make this reasoning clear to any readers. 