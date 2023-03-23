class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        p1 = 0
        p2 = 0
        maxlen = 0

        while p2 < len(s):
            c = s[p2]
            p2 += 1
            if c not in charset:
                charset.add(c)
                maxlen = max(maxlen, len(charset))
            else:
                while s[p1] != c:
                    charset.remove(s[p1])
                    p1 += 1
                p1 += 1
        
        return maxlen