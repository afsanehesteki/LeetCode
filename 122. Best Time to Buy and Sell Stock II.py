class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        prof= 0 
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff>=0 :
                prof +=diff
        return prof

        
