from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        answer = 0
        hasOdd = False
        for v in c.values():
            if v%2 == 0:
                answer += v
            else:
                hasOdd = True
                answer += (v - 1)
        
        if hasOdd:
            answer += 1

        return answer