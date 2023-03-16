class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        isPal = True

        print("0".isalpha())
        
        while p1 < len(s) and not s[p1].isalpha() and not s[p1].isnumeric():
            p1 += 1      
        while p2 >=0 and not s[p2].isalpha() and not s[p2].isnumeric():
            p2 -= 1
        
        while p1 < p2 :
            if s[p1].lower() != s[p2].lower():
                return False
            
            p1 += 1
            p2 -= 1
            while p1 < len(s) and not s[p1].isalpha() and not s[p1].isnumeric():
                p1 += 1
            while p2 >=0 and not s[p2].isalpha() and not s[p2].isnumeric():
                p2 -= 1
        
        return True
