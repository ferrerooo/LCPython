class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        answer = 0
        for l in reversed(range(1, n)):
            visited = set()
            for i in range(0, n-l+1):
                if s[i:i+l] in visited:
                    answer = l
                    break
                else:
                    visited.add(s[i:i+l])
            if answer > 0:
                break
        
        return answer
        