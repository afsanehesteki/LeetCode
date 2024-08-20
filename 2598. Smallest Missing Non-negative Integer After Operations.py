class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num % value]+=1
        print(freq)
        i = 0
        while freq[i%value]:
            freq[i%value]-=1
            i+=1
        return i
