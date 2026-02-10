class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for i in range(0,len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

prices = [7,1,5,3,6,4,8]
     
obj = Solution()
result = obj.maxProfit(prices)
print(result)
        
