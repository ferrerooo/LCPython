from collections import defaultdict

class TicTacToe:

    def __init__(self, n: int):
        self.rowplayer1 = defaultdict(int)
        self.colplayer1 = defaultdict(int)
        self.rowplayer2 = defaultdict(int)
        self.colplayer2 = defaultdict(int)
        self.cross1player1 = 0
        self.cross2player1 = 0
        self.cross1player2 = 0
        self.cross2player2 = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rowplayer1[row] += 1
            self.colplayer1[col] += 1
            if row == col:
                self.cross1player1 += 1
            if row + col == self.n - 1:
                self.cross2player1 += 1
            
            #print(f'{self.rowplayer1[row]}__{self.rowplayer1[col]}__{self.cross1player1}__{self.cross2player1}')
            if self.rowplayer1[row] == self.n or \
            self.colplayer1[col] == self.n or \
            self.cross1player1 == self.n or \
            self.cross2player1 == self.n:
                return 1
        else:
            self.rowplayer2[row] += 1
            self.colplayer2[col] += 1
            if row == col:
                self.cross1player2 += 1
            if row + col == self.n - 1:
                self.cross2player2 += 1
            
            #print(f'{self.rowplayer2[row]}__{self.rowplayer1[col]}__{self.cross1player1}__{self.cross2player1}')
            if self.rowplayer2[row] == self.n or \
            self.colplayer2[col] == self.n or \
            self.cross1player2 == self.n or \
            self.cross2player2 == self.n:
                return 2
        
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)