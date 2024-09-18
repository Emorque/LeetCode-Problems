1. Share questions you would ask to help understand the question:
- By reversing the bits, do you mean like reversing a string, or just reversing the individual bits themselves?
- So instead of getting 3 as an input, n would instead be 011?
- Am I returning the bits reversed, or the new n that it represents?
- How many bits can I expect from n?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Bit manipulation

3. Write out in plain English what you want to do: 
- Going through an example, I figured that the following order of sequences helps to build an output int
  - get the leftmost bit of n with and: n & 1
  - set that to output by using the or operator: output & bit
  - shift output to the left once
  - shift n to the right once
  - Now I can grab the new leftmost bit from n and set it to the new rightmost bit in output

4. Translate each sub-problem into pseudocode:
- Do what I explained in 3., except that it'll be in a loop that iterates 32 times (length of n)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            bit = n & 1
            
            output = output << 1
            output = output | bit

            n = n >> 1            
        return output -->

- output needs to be shifted first by 1 before adding that bit

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm is doen with no additional space, and done linearly
- One weak area is that it be confusing what is happening if the person doesn't have exposure to bits