1. Share questions you would ask to help understand the question:
- Could prices be negative numbers?
- Will prices never have a negative length?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash Map (Unlikely)
- Bottom-up (Likely)

3. Write out in plain English what you want to do:
- The goal is to get the max profit, from buying the stock on day i, and selling on a day after i
- What could be done, is that as I iterate through the prices list, I keep track of the current min price, and the current max profit
- Since the price list is guarenteed to be between a length of 1 - 10^5, the current minPrice can be set to prices[0]
- Then as I iterate, check the current price, calculating it with the minPrice, and then adjusting the maxPrice variable if a new maxPrice is found
- After iterating through the whole list, return the maxPrice

4. Translate each sub-problem into pseudocode:
- Initialize two variables
    - minPrice to prices[0]
    - output to 0
- iterate through the list:
    - set minPrice to min(minPrice, prices[i])
    - set output to max(output, prices[i] - minPrice)
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice: int = prices[0]
        output: int = 0

        for price in prices:
            minPrice = min(minPrice, price)
            output = max(output, price - minPrice)
        
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, since the solution is built over one traversal, only one traversal through prices is needed
- One weak area is that it could be improved to be more readable with perhaps better variable names and without min, max