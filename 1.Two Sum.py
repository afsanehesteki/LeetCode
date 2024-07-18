#1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = dict()
        for i in range (len(nums)):
            temp = target - nums[i]
            if temp in mydic: 
                return [i , mydic[temp]]
            mydic[nums[i]] = i
