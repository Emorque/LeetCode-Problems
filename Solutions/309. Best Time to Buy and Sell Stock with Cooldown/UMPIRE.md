1. Share questions you would ask to help understand the question:
- What is the range of length that prices can be?
- Can there be negative prices?
- Can I pass a day by not buying or selling, despite being able to (off cooldown)?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- By simplifying the problem, bascially at each day, we can either buy, sell, or wait/be on cooldown
- Another thing is that selling has to come before buying, and if we sell, then we have to go forward two days, before being able to either buy or wait
- In other words, at each index, I am either buying or selling, and depending on those choices, the path I can take diverges
- This leds to a decision tree with there are n levels, and the 2 choices at each node (buy/sell, wait/cd), which can get costly (2^n)
- An alternative route is to try have store some memory
- As said earlier, at each day, there are two choices
  - So, what we there is a struture that matches both choices on a day individually to some maxProfit
    - This can be done with a map where the key is (day, buying), and the value is the maxProfit
- So, depending on whether I enter the day in a buying or selling state, I recursively call the function, to the opposing state and if I decide to wait. One day/choice diverges into two. And what I get back, I set the max to the hashmap and return it 

4. Translate each sub-problem into pseudocode:
- Initialize a profits hashmap

- create a helper function that takes in the day index and whether I am buying:
  - if day is out of bounds:
    - return 0
  - if (index, state) is already set in the hashmap:
    - return it, no need to compute it again
  
  - if buying:
    - buy = helper((i + 1), False) - prices[i] substract the current price as we are buying
    - cooldown = helper((i + 1), True)
    - hashmap[(i, buying)] = max(buy, cooldown)
  - else:
    - sell = helper((i + 2), True) + prices[i] The next time we can buy is two days from now, and add the current price as we have gained some money. We are in a state of selling, we can choose to sell and gain prices[i] or wait and sell the next day
    - cooldown = helper((i + 2), False)
    - hashmap[(i, buying)] = max(sell, cooldown)
  - return hashmap[(i, buying)]

- return helper(0, True)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = {}

        def dfs(day, buying):
            if day >= len(prices):
                return 0
            if (day, buying) in profits:
                return profits[(day, buying)]
            
            if buying:
                buy = dfs(day + 1, False) - prices[day]
                cooldown = dfs(day + 1, True)
                profits[(day,buying)] = max(buy, cooldown)
            else:
                sell = dfs(day + 2, True) + prices[day]
                cooldown = dfs(day + 1, False)
                profits[(day, buying)] = max(sell, cooldown)
            return profits[(day, buying)]
        
        return dfs(0, True) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a hashmap is used to document the profits that are possible on a day depending on whether I have bought or sold on that day. That way, I can start from the left, reach the right, and build back up the max profit
- One weak area is that this solution may not be clear and there is an optimization to be made. A hashmap is used, but since there is only a defined list of potential states I can be in, buying, selling, cooldown; a list of lists can be used