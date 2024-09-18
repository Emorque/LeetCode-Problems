1. Share questions you would ask to help understand the question:


2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Math (Likely)
- Bit Manipulation (Neutral)

3. Write out in plain English what you want to do: 
- So, since there is a chance that the reversed integer goes out of bounds, then I do need to make sure that before I make any changes to my output, that I am within the bounds
- Also, since I am working with ints, instead of using some index like with an array for traversal, I could use //10 and * 10 as ways to build and destroy digits
- If I can build the output without ever returning 0, return that int

4. Translate each sub-problem into pseudocode:
- initialize an output to 0 
- get the bound, depending on if x is a negative or positive number 
- set x to its absolute
- while x is no longer 0:
    - if output * 10 > bound:
        - we cannot add further, so return 0
    - output *= 10, shifting the digits to the left
    - ouptut += x % 10
    - x = x // 10, shifting the digits to the right (would be 0 at the end)

- return output * -1 if x was negative, else return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        if x >= 0:
            bound = (2 ** 31) - 1
        else:
            bound = 2 ** 31
        
        x = abs(x)
        output = 0

        while x != 0:
            if output * 10 > bound:
                return 0
            output *= 10
            output += x % 10
            x = x //10

        return output * (-1) if negative else output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the solution is built and always checks the bounds before ever getting to an int that would be out of bounds and potentially breaking the program
- One weak area is that there is a lot of setup, setting up abs, the bound, and seeing if x was negative before the work starts