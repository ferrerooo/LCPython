class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        p1 = 1
        p2 = n-1
        answer = 0
        while p1 <= p2:
            mid = (p1+p2)//2
            if self.hasRepeatStr(s, mid):
                answer = max(answer, mid)
                p1 = mid+1
            else:
                p2 = mid-1
        
        return answer
    
    def hasRepeatStr(self, s: str, mid: int) -> bool:
        visited = set()
        for i in range(0, len(s)-mid+1):
            curStr = s[i:i+mid]
            if curStr in visited:
                return True
            else:
                visited.add(curStr)
        return False