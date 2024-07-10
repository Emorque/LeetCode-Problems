1. Share questions you would ask to help understand the question:
- Will there be a case where we have more piles than h?
- How many times can we go through piles?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Binary Search (Likely)
- Hashmap (Unlikely)
  
3. Write out in plain English what you want to do: 
- Get the max number of bananas from the piles and have an initial min number of 1. Use binary search to set a mid number can see how long eating mid amount of bananas takes. Depening of the result, adjust the min, max, and mid till min and max intersect. Then return min. 

4. Translate each sub-problem into pseudocode:
- A way to brute force this would be to start from 1, and iterate through piles, checking piles[i] / 1 and then adding that to some count variable. Do this for each pile in piles, and then check it the hours variable is equal to h. 
- If it less, than increment 1 to 2 and then do it over and over again. 
- However, since we have constraints such as 1 <= piles[i] <= 10^9, brute forcing it isn't the best option.
- What we could do, is maybe getting the max number of bananas that are in a pile, setting that as our maxBanana variable. our minBanana could start as 1
- Then we do "binary search" , setting a midBanana to be minB + ((maxB - minB) / 2)
- Set a while loop that continues while minB < maxB
    - Do the steps mentioned in bullet point 1, calculating the number of hours for midBanana. If hours <= h, set maxB to midB 
    - Else, set minB to midB + 1
- Now, return minB

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minBanana = 1
        maxBanana = max(piles)
        
        while minBanana < maxBanana:
            midBanana = minBanana + ((maxBanana- minBanana) // 2)
            hours = 0
            for pile in piles:
                hour = pile // midBanana
                if pile % midBanana:
                    hour += 1
                hours += hour
            if hours <= h:
                maxBanana = midBanana
            else:
                minBanana = midBanana + 1
        return maxBanana -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it does a binary search alogrithm to reduce the amount of checks needed for especially high values of piles[i] and h
- One weak area is that I forgot that the method ceil() exists. Using this could have reduced the need for that nested if statement and I could have reworked my midBanana right after the while loop to use less math to acheive the same result. 