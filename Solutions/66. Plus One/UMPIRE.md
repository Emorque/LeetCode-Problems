1. Share questions you would ask to help understand the question:
- Can there negative integers?
- Are the elements in digits, ints themselves
- What is the expected range that digits can be?
- Can I return the digits array if the number of digits stays the same

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely


3. Write out in plain English what you want to do: 


4. Translate each sub-problem into pseudocode:


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- Thanks to [1] +, I can just add an extra digit to the left of the digits list, as if I had added a carry 1 doing addition