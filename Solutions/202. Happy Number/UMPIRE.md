1. Share questions you would ask to help understand the question:


2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely


3. Write out in plain English what you want to do: 
- Use a set to keep track of seen numbers
- If a number is already in the set, then I know that I have entered into a cycle, so I can return False
- Else if this never happens, return True evantually when the number equals 1

4. Translate each sub-problem into pseudocode:


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            happy = 0
            while n != 0:
                happy += ((n % 10) ** 2)
                n = n // 10
            n = happy
        return True -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution uses a set to track already seen numbers so that an endless loop isnt entered
- One weak area is that this can be simplified by converting n to a string and getting digits that way instead of using % 