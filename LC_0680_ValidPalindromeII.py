class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1] != s[p2]:
                if self.isPal(s[p1:p2]) or self.isPal(s[p1+1:p2+1]):
                    return True
                else:
                    return False
            
            p1 += 1
            p2 -= 1
        
        return True
    
    def isPal(self, s):
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True