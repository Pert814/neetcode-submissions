class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 兩步一定比一步一步走便宜 => 不可能一次走兩個1步
        # 做一個 a, b隨著遍歷一路累積上去
        a, b = cost[0], cost[1]
        for cost in cost[2::]:
            print(cost)
            a, b = b, cost + min(a,b)
        return min(a,b)