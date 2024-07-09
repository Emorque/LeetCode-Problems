1. Share questions you would ask to help understand the question:
- How large can n get?
- Can n be halved?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- Stack (Unlikely)
  
3. Write out in plain English what you want to do: 
- The biggest thing to take note of is this constraint: -2^31 <= n <= 2^31-1
- This means that if we were to do n recursive calls, it would quickly get out of hand
- Since we are dealing with powers, we can use math to half the number of recursive calls needed. 
    - for example: if we have 2^16. Instead of making 16 recursive calls, we can make 8, and then multiply that result with itself because 2^16 is equal to 2^8 * 2^8
- Therefore, we just need base cases and this logic above to get the answer. 

4. Translate each sub-problem into pseudocode:
- if n is equal to 0, return 1
- if n is equal to 1, return x
- if n is equal to -1, return 1/x

- then we do that halving logic from 3. and do:
- answer = self.myPow(x, n//2)
- Then we multiply it by itself. 
- Add a conditional to check if n is even or odd. If n is odd, multiply again by just x. 
- For example, if we have 2^17, we would then need 2^8 * 2^8 * 2
- return the end product 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        elif n == 1: return x
        elif n == -1: return 1/x

        answer = self.myPow(x, n // 2)
        if (n % 2):
            return answer * answer * x
        else:
            return answer * answer -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it uses math to use less recursive calls
- One weak area is that we are since we are using recursive, we are using memory. An alterative route could be to utilize a while loop to do the math in place. 