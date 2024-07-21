class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #1 space: o(n) since counter uses space like dictionary
        count = collections.Counter(nums).most_common(1)
        return count[0][0]
        #2 since there is always a majority. Space : O(1)
        maj = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == maj:
                count+=1
            else:
                count-=1
            if count<0:
                count=1
                maj=nums[i]
        return maj
