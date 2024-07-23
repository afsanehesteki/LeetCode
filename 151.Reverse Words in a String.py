class Solution:
    def reverseWords(self, s: str) -> str:
        # O(n) space
        # arr = s.split()
        # arr = arr[::-1] #arr.reverse() 
        # return  " ".join(arr)
        #[::-1] reverse all char in string, or revese elements of an array

        # O(1) space
        return " ".join(s.split()[::-1])
