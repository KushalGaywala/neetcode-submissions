class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        profit = 0

        for price in prices:
            if price <= mini:
                mini = price

            diff = price - mini

            if profit < diff:
                profit = diff
        
        return profit