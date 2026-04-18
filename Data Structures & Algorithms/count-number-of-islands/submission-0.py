class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        islands=0

        def dfs(r,c):
            #if out of bounds or water 
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=='0':
                return 
            grid[r][c]='0'#mark as visited land as water so that we do not visit again

            #explore complete island
            dfs(r+1,c)#down
            dfs(r-1,c)#up
            dfs(r,c+1)#right
            dfs(r,c-1)#left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    dfs(r,c)#find island
                    islands+=1
        return islands
        