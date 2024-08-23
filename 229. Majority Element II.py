class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #possible number of elements that can appear more than ⌊ n/3 ⌋ times => 2
        # So we can keep a hashmap of size 2
        m = collections.defaultdict(int)
        for n in nums:
            m[n]+=1
            if len(m) >2:
                for key in list(m.keys()): # To avoid "dictionary changed size during iteration error", use "list" to cast dictionary items to list 
                    m[key]-=1
                    if m[key]==0:
                        m.pop(key)

        for key in list(m.keys()):
            realtotal=0
            for n in nums:
                if n==key:
                    realtotal+=1
            if realtotal<= len(nums)//3:
                m.pop(key)

        return m.keys()

