class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height)-1
        maxLSoFar = height[0]
        maxRSoFar = height[r]
        res = 0 
        while l<=r: 
            if maxLSoFar<=maxRSoFar:
                curH = max (maxLSoFar - height[l] , 0) # to prevent negative number I add max ( ... , 0 )
                maxLSoFar = max (maxLSoFar , height[l])
                l+=1
                res+= curH
            else: 
                curH = max(maxRSoFar - height[r], 0) 
                maxRSoFar = max (maxRSoFar , height[r])
                r-=1
                res+= curH
        
        return res
