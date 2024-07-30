class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = dict()
        dic = defaultdict(list)
        res = []
        for word in strs:
            sortedword = "".join(sorted(word))   
            dic[sortedword].append(word) 
            # if sortedword in  dic:
            #     dic[sortedword].append(word) 
            # else:
            #    dic[sortedword] = [word]
        for value in dic.values():
            res.append(value)
        return res
