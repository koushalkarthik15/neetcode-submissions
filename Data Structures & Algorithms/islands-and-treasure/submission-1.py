class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        m,n=len(grid),len(grid[0])
        dire=[(1,0),(-1,0),(0,1),(0,-1)]
        q=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            row,col=q.popleft()
            for dr,dc in dire:
                nr,nc=dr+row,dc+col
                if (0<=nr<m and 0<=nc<n and grid[nr][nc]==INF):
                    grid[nr][nc]=grid[row][col]+1
                    q.append((nr,nc))