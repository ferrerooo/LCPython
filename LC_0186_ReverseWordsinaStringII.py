class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp
            p1 += 1
            p2 -= 1
        
        p1 = 0

        while p1 < len(s):
            p2 = p1
            while p2 < len(s) and s[p2] != ' ':
                p2 += 1
            a = p1
            b = p2 - 1
            while a < b:
                temp = s[a]
                s[a] = s[b]
                s[b] = temp
                a += 1
                b -= 1
            p1 = p2+1
        
        return