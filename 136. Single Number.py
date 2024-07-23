class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #1 using set
        #myset = set()
        #for n in nums:
        #    if n in myset:
        #      myset.remove(n)
        #   else: 
        #       myset.add(n)
        #return myset.pop()

        #2 XOR
        res = 0 # 0 XOR any number = number
        # [3,5,3] ---> res = 3^5^3 = 0 ^5 = 5
        for n in nums:
            res = res ^ n
            print(res)
        return res
        
