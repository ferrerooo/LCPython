class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [ [0 for j in range(n)] for i in range(n) ]
        answer = 0

        for i in range(1,n):
            if s[0] == s[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = 0

        for i in range(1, n-1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    answer = max(answer, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return answer
