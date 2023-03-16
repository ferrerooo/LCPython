class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        matrix = [[0 for _ in range(n)] for _ in range(n)] 

        output = 0

        for i in range(n):
            matrix[i][i] = 1
            output += 1

        
        for i in range(1, n):
            if s[i-1] == s[i]:
                matrix[i-1][i] = 1
                output += 1

        for i in range(2, n):
            for j in range(0, n-i):
                if s[j] == s[j+i]:
                    if matrix[j+1][j+i-1] == 1:
                        matrix[j][j+i] = 1
                        output += 1

        return output