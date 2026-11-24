class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=collections.deque()
        fresh=0
        level=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        dire=[[0,1],[0,-1],[1,0],[-1,0]]
        while fresh>0 and q:
            length=len(q)
            for i in range(length):
                r,c=q.popleft()
                for dr,dc in dire:
                    row,col=r+dr,c+dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1):
                        grid[row][col]=2
                        q.append((row,col))
                        fresh-=1
            level+=1
        return level if fresh==0 else -1