1. Share questions you would ask to help understand the question:
- What are the ranges that x and n can be?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely


3. Write out in plain English what you want to do: 


4. Translate each sub-problem into pseudocode:
- One thing that can be done, is if n is a negative, we can treat it as positive, and at the end, return 1/result.
    - for example: 2 ^ -3 = 1/2^3



5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        if n > 0:
            positive = True
        else:
            positive = False

        halfPower = self.myPow(x, abs(n)//2)
        answer = halfPower * halfPower
        
        if n % 2 == 1:
            answer *= x
        
        return answer if positive else 1/answer

         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm is an efficient one with a time of O(logn) since the word is split in half because of how math works
- One weak area is that this solution may not be clear one one doesn't know that a number to a power can be split up