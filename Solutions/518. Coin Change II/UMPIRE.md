1. Share questions you would ask to help understand the question:
- Can there be negative valued coins?
- Can there be individual coins that are greater than the desired amount? 
- What is the range of the number of coins we can have in the list?
- Can there be coins of the same value?
- What is the range that amount can be?
- What if amount is 0?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP 

3. Write out in plain English what you want to do: 
- A dfs solution with a decision tree can be made to solve this problem, but it can get expensive 
- At first I was thinking of using a cache where I would have an array of length coins + 1, and each index would map to the number of unique combinations it would take to get to that amount
  - It was close but it wasn't enough, instead of just knowing the amount and combinations, I also need to know the number of combinations. 
    - I need some way to not include duplicate combinations and this should solve that issue
  - To do this, I would need to use a 2d grid, where the x axis is the amount list I described before, and the y axis is the value of all of the coins in the coins list

- I know that the default case is 1, for the amount 0
- As for getting the combinations of for example amount: 4, I would take the current coin that I have. 
  - See if the coin is <= the amount, 5 wouldn't work here for example
    - If I have 3, then I would get 4 - 3 = 1. Then I would check what the number of unique combinations 3 can make to get 1. This would be 0, so 4 would also be 0
  - Then, when moving to the next coin, I follow the same process, except I also need to add the cell above to my current cell, so that as I go down the rows, I am bringing the total number of unique combinations down.  

4. Translate each sub-problem into pseudocode:
- Initialize a grid that is the length of amount + 1, and a height of len(coins) + 1, with each value set to 0, except the first index, which is set to 1

- for i in range(1, amount + 1):
  - for j in range(1, len(coins) + 1):
    - difference = amount - coins[j - 1]
    - if difference >= 0:
      - grid[i][j] += grid[i][difference]
    - grid[i][j] += grid[i - 1][j]

- return grid[-1][-1]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        grid = []
        for i in range(len(coins) + 1):
            grid.append([0] * (amount + 1))
            grid[i][0] = 1
        
        for r in range(1, len(coins) + 1):
            for c in range(1, amount + 1):
                difference = c - coins[r - 1]
                if difference >= 0:
                    grid[r][c] += grid[r][difference]
                grid[r][c] += grid[r - 1][c]
        
        return grid[-1][-1] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- The strong area is that this algorithm uses a grid to store all of the unqiue combinations of each amount for each coin, which answers the smaller question: how many unqiue combinations can make up 1 to amount
- The weak area is that once I have gone down two rows and iterate to the next one, the row left behind is no longer being used. If I could optimize this solution, I would try to use only two rows of length (amount + 1), instead of len(coins) + 1 rows