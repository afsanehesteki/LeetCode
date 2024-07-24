class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #1 Extra memory
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for c in s: 
            dic1[c]= dic1[c] +1
        for c in t: 
            dic2[c] =dic2[c] +1
        for key in dic1:
            if dic1[key] != dic2[key]:
                return False
        return True

        #2 using Counter
        return Counter(s) == Counter(t)

        #3 sort
        return sorted(s) ==  sorted(t)  
            

