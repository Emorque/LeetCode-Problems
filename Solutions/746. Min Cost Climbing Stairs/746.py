class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costLength = len(cost)
        for i in range(2, costLength):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return min(cost[costLength - 1], cost[costLength -2])