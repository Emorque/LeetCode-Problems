1. Share questions you would ask to help understand the question:
- What are the ranges of ints that a and could b?
- Do I have to worry about going out of bounds with my sum?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Bit Manipulation (Likely)

3. Write out in plain English what you want to do: 
- Getting the xor and and values of a and b is equivalent to adding them together, with the and specifically representing the carry values
- Once and is a 0, meaning that there is no more carry, then the value within xor will be the final sum
- Until this, this loop is repeated

4. Translate each sub-problem into pseudocode:
- While the and is not 0 
- Set a temp to be the carry
- set a to a xor b
- set b to the temp 

- once b is equal to 0, return a

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int temp = (a & b) << 1; //This is the carry
            a = a ^ b;
            b = temp;
        }
        return a;
    }
} -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- Do this in Java as Python's handling on integers/bits won't let this work (python will mess up with negatives) (Time limit exceeded)