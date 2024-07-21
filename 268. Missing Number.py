class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using set()
        # s = set(nums)
        # for n in range(len(s)+1):
        #     if n not in s: 
        #         return n

        # using math
        total = len(nums) * (len(nums) +1) //2
        subtotal = 0
        for n in nums:
            subtotal+=n
        return total - subtotal
