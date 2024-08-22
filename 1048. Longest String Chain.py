class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # time: O(n * l * l) --> n= size of words , l = avg length of every word . Seconf l is beacuse of recursive function
        wordset= set(words)
        words.sort(reverse=True , key=len) #sorted_words = sorted(words,reverse=True , key=len) #Does not modify original array

        memo={}
        def dfs(word):
            #if len(word) ==1:
            #   return 0
            if word not in wordset:
                return 0
            if word in memo:
                return memo[word]
            mx = 0
            N = len(word)
            for i in range(N):
                newword = word[0:i] + word[i+1:] #instead of adding a char, remove a char, since removing is easier 
                mx= max(mx , dfs(newword)+1)
            memo[word] = mx
            return mx

        for word in words:
            dfs(word)
        
        return max(memo.values())
