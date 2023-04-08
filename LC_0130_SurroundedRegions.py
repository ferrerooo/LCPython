class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            if board[i][n-1] == 'O':
                self.bfs(board, i, n-1)
        
        for j in range(n):
            if board[0][j] == 'O':
                self.bfs(board, 0, j)
            if board[m-1][j] == 'O':
                self.bfs(board, m-1, j)

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
                else:
                    pass
        
        return
    
    def bfs(self, board, a, b):

        m = len(board)
        n = len(board[0])

        q = collections.deque()
        q.append((a,b))

        while q:
            cur = q.popleft()
            x = cur[0]
            y = cur[1]

            if board[x][y] == 'A':
                continue
            
            board[x][y]= 'A'

            if x+1 < m and board[x+1][y] == 'O':
                q.append((x+1, y))
            if y+1 < n and board[x][y+1] == 'O':
                q.append((x,y+1))
            if x-1 >= 0 and board[x-1][y] == 'O':
                q.append((x-1, y))
            if y-1 >= 0 and board[x][y-1] == 'O':
                q.append((x, y-1))
            
        return
            