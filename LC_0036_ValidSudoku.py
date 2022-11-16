class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            aset = set()
            for col in range(9):
                if board[row][col] in aset and board[row][col] != '.':
                    return False
                else:
                    aset.add(board[row][col])
        
        for col in range(9):
            aset = set()
            for row in range(9):
                if board[row][col] in aset and board[row][col] != '.':
                    return False
                else:
                    aset.add(board[row][col])
        
        for row in list(range(9))[::3]:
            for col in list(range(9))[::3]:
                aset = set()
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] in aset and board[row+i][col+j] != '.':
                            return False
                        else:
                            aset.add(board[row+i][col+j])
        
        return True