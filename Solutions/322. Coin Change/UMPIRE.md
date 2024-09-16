1. Share questions you would ask to help understand the question:
- Are all the elements in coins nonzero and positive?
- Can an amount be 0?
- Can amount be negative?
- Can we have zero coins, or is there always at least one?
- Can there be coins of the same value?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Backtracking (Unlikely)
- Greedy (Unlikely)
- DP (Likely)

3. Write out in plain English what you want to do: 
- I tried to picture this as a decision tree.
  - And if I decided to explore this option, it looked like for every decision, I could make n decisions if the current sum would be less than amount, which would get expensive really quickly

- However, when drawing out a decision tree, I realized that there are some moments when I would have to redo decisions for amounts I've already found
- So, to optimize this approach, I think using some data structure to hold some of these results would be useful.
  - So that I don't have to redo work

- By getting the min amount of coins for each potential amount up to amount, I can then store the number of coins and slowly build up to that amount we want

4. Translate each sub-problem into pseudocode:
- Initialize a list with a len of amount + 1. The reason is that there is no way to not know if I need to now how many coins can lead to 2 when I am on amount 4444
- Initialize index 0 to 0 as a base case
- Enter a for loop that iterates amount times + 1
  - for each coin:  
    - if currentAmount - coin >= 0:
      - the current coin can be used to lead to current Amount
      - list[currentAmount] = min(list[currentAmount], 1 + list[currentAmount - coin])
- return list[amount] if list[amount] != 100000000000(default) else -1  

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [(amount + 1)] * (amount + 1)
        cache[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])
        
        return cache[amount] if cache[amount] != amount + 1 else -1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this alfgorithm uses a building up approach with a cache to save done work, so that when an amount is set, it can be referenced
- One weak area is that it makes sense after the diagrams I drew and explanination I gave, so just the code itself doesn't do a good job explaining how this solution works