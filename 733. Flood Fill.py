class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        mainColor = image[sr][sc]
        def dfs (r, c):
            if r<0 or c<0 or r>row-1 or c>col-1 or image[r][c] == color or image[r][c]!=mainColor:
                return
            image[r][c] = color
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r, c+1)
            
        dfs(sr , sc )
        return image
        

        
