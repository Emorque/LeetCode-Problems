1. Share questions you would ask to help understand the question:
- Will the initial number ever negative?
- What is the highest potential input?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- Dynamic Programming (Likely)

3. Write out in plain English what you want to do: 
- The way that the question is laid out, looks to me like it can be set up for recursion.
- There are two base cases provided in the question, if the input is 0, return 0, and when the input is 1, return 1
- Then return the sum of recursively calling fib on n-1 and n-2

5. Translate each sub-problem into pseudocode:
- Base case: if n <= 1:
    - return n
- return fib(n-1) + fib(n-2)

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)-->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm is very readible and clear to follow
- One weak area is that it takes up memory with the recursion stack
    - There is one unique solution that doesn't use the recusion stack like I did:
    - " a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b"
    - It is a very creative solution that builds the solution over a loop
