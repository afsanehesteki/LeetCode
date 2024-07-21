class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maxProf = 0
        for i in range(1, len(prices) ):
            minimum= min(prices[i],minimum) 
            maxProf =max (maxProf , prices[i] - minimum)    
        return maxProf
        
