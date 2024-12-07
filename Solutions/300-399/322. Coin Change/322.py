from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = [float("inf")] * (amount + 1)
        total[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                total[i] = min(total[i], total[i - c] + 1)

        return total[amount] if total[amount] != float("inf") else -1