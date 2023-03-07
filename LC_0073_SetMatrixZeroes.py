class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row0Has0 = False
        col0Has0 = False

        for i in range(m):
            if matrix[i][0] == 0:
                col0Has0 = True
                break
        
        for i in range(n):
            if matrix[0][i] == 0:
                row0Has0 = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
            
        if row0Has0:
            for i in range(n):
                matrix[0][i] = 0
        
        if col0Has0:
            for j in range(m):
                matrix[j][0] = 0
        
        return
