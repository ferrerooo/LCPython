class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        small = min(m, n)
        answer = []

        for r in range(small//2):
            for l in range(r, n-1-r):
                answer.append(matrix[r][l])
            for i in range(r, m-1-r):
                answer.append(matrix[i][n-r-1])
            for l in reversed(range(r+1, n-r)):
                answer.append(matrix[m-1-r][l])
            for i in reversed(range(r+1, m-r)):
                answer.append(matrix[i][r])
        
        if small%2 != 0:
            r = small//2
            if n > m:
                for i in range(r, n-r):
                    answer.append(matrix[r][i])
            else:
                for i in range(r, m-r):
                    answer.append(matrix[i][r])
        
        return answer