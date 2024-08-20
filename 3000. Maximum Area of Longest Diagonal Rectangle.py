class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longestDiagonal = 0
        maxArea =0 
        for rec in dimensions:
            diagonal = math.sqrt(rec[0]**2 + rec[1]**2)
            area = rec[0] * rec[1]
            if (diagonal > longestDiagonal) or (diagonal==longestDiagonal and area > maxArea) :
                longestDiagonal = diagonal
                maxArea = area

        return maxArea
