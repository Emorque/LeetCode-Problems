# decision tree with caching
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} #index, amount: res

        def helper(index, currAmount):
            if (index, currAmount) in cache:
                return cache[(index, currAmount)]
            if currAmount == amount:
                cache[(index, currAmount)] = 1
                return 1
            if currAmount > amount or index == len(coins):
                cache[(index, currAmount)] = 0
                return 0
            res = 0

            # len(coins) ^ amount time
            # for i in range(index, len(coins)):
            #     res += helper(i, currAmount + coins[i])
            
            #len(coins) * amount time
            res = helper(index, currAmount + coins[index]) + helper(index + 1, currAmount)
            
            cache[(index, currAmount)] = res
            return res

        return helper(0, 0)