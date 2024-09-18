1. Share questions you would ask to help understand the question:
- What is the range of numbers that n can be?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Bitwise

3. Write out in plain English what you want to do: 
- Since we are dealing with bits, the first thoughts that came to me, was to use some bit operators
- After trial and error, I thought of using the >> operator, which bascially shifts the bits to left
    - In doing so, this bascially divides the number by 2, but if the right most bit was 1, the number becomes itself / 2 - 1, because the right most bit is a value of 1: 2^0 = 1

4. Translate each sub-problem into pseudocode:
- Intiailize some count variable

- While n != 0:
    - newN = n >> 1
    - if n == newN * 2 + 1. Then the rightmost bit was a 1, and so, was removed
        - count += 1
    - n = newN
- return count

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            newN = n >> 1
            if n == (newN * 2) + 1:
                count += 1
            n = newN
        return count -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution is done in linear time, basically the number of bits that are in n
- One weak area is that while this solution works, it can furhter be optimized. I made this solution more complicated than I needed to. 
    - I could instead just do if n & 1 == 1, which basically does the rightmost bit of n & 1
        - If it results in 1, then the rightmost bit has a 1. If it doesn't, then the rightmost bit is 0
            - Then, I could increment count by 1
        - Then I can do n >> 1 like before

- *I included the more optimal solution in the py file