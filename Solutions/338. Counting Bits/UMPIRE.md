1. Share questions you would ask to help understand the question:
- So will the binary be read from right to left?
- What are the ranges that n can be?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Bitwise (Likely)

3. Write out in plain English what you want to do: 
- After drawing out the array for 16, I realized that there is a pattern here
  - When the number is a power of 2, the value is always 1, which makes sense since in bit notation, every index is a power of 2
  - When a number has a 1 in the leftmost bit position, I can always just refer to the previous number and add one to it
  - When a number has a 0 in the leftmost bit position, then I can either:
    - get the previous value and set it to my current value
    - get the previous value - 1 and set it to my current value

    - these two cases happen right after the other, with the first happening first whenever 1 is set for a value

4. Translate each sub-problem into pseudocode:
- Initialize an array of size n + 1, with each value set at 0
- subtract = False
- power = 2
- for i in range(1, n + 1):
  - if 2 ** power == i:
    - nums[i] = 1
    - power += 1
    - subtract = False
    - continue
  - if i & 1 == 1:
    - nums[i] = nums[i - 1] + 1
  - else:
    - if subtract:
      - nums[i] = nums[i - 1] - 1
    - else:
      - nums[i] = nums[i - 1]

- return the nums array

- This doesn't work as I thought for cases past 16 

- There is anothe pattern that I can try that is simplier
- So the n & 1 case still can work here
- There is another case, for if n doesn't pass for the previous case, 
  - Then n's value is actually the same as the value set at n//2
- n & 1 gets the odd numbers, which always takes previous and adds 1
- If false, that gets the even numbers, which is has the same 1s as n // 2

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1 == 1:
                nums[i] = nums[i - 1] + 1
            else:
                nums[i] = nums[i //2]
        return nums -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this is like DP solution, since previous work is used to save needing to do duplicate work
- One weak area is that I was only able to figure out these two if statements by drawing out the bit representations of multiple numbers, so it may not be clear why this works without it or an explanation