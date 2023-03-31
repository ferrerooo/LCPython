from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        answer = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                answer += 1
                q = deque()
                q.append((i,j))
                while len(q) > 0:
                    x,y = q.popleft()
                    if grid[x][y] != '1':
                        continue
                    grid[x][y] = '2'
                    if x+1 >= 0 and x+1 < m and y >= 0 and y < n and grid[x+1][y] == '1':
                        q.append((x+1, y))
                    if x >= 0 and x < m and y+1 >= 0 and y+1 < n and grid[x][y+1] == '1':
                        q.append((x, y+1))
                    if x-1 >= 0 and x-1 < m and y >= 0 and y < n and grid[x-1][y] == '1':
                        q.append((x-1, y))
                    if x >= 0 and x < m and y-1 >= 0 and y-1 < n and grid[x][y-1] == '1':
                        q.append((x, y-1))
        
        return answer             
                    