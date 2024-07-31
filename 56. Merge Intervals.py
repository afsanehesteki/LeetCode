class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = output[-1][1] 
            if start <= lastEnd :
                output[-1][1] = max(lastEnd, end) # to cover [[1, 10],[5, 7] , not only regular [[1,6] , [5,7]]
            else: 
              output.append([start,end])  # [[1,4] , [6,10]]
        return output
