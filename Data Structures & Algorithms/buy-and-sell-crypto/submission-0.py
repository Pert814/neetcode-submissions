class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max0, l, r = 0, 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                dif = prices[r] - prices[l]
                max0 = max(max0, dif)
            else:
                l = r 
            r += 1 
        return max0