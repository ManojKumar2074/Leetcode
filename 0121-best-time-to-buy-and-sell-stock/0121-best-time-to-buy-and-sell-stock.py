class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        profit = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] - mini > profit:
                profit = prices[i] - mini
        return profit
                
            
