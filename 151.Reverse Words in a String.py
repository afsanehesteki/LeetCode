class Solution:
    def reverseWords(self, s: str) -> str:
        splits = s.split()
        splits.reverse()
        res = " ".join(splits)
        return res


