class Solution:
    def climbStairs(self, n: int) -> int:
        case1 = 1
        case2 = 1

        for i in range(n - 1):
            total = case1 + case2
            case1 = case2
            case2 = total
        return case2