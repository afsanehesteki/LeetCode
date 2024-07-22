class Solution:
    def isPalindrome(self, x: int) -> bool:
        #1 convert x to string and reveres it
        # st = str(x)
        # rev = st[::-1] # reverse a string or an array. We cannot use Reveres function for String
        # if st == rev:
        #     return True
        # return False
        #2 not using string
        if x<0: 
            return False
        res = 0
        orig = x
        while x>0:
            rem = x % 10
            x = x // 10
            res = res *10 + rem
        if res == orig:
            return True
        return False



