class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n !=1):
            res = 0
            while n>0:
                res = res + (n%10) * (n %10)
                n = n//10
            if res in seen:
                return False
            seen.add(res)
            n = res
        return True
        # maybe not the best since using extra array
        # seen = set()
        # res = n
        # while (res !=1):
        #     s = str(res)
        #     arr = [ int(d) for d in s]
        #     res = 0
        #     for d in arr:
        #         res = res + d*d
        #     if res in seen:
        #         return False
        #     seen.add(res)
        # return True
