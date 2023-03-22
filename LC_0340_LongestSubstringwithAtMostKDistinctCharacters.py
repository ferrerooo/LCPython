class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        p1 = 0
        p2 = 0
        charMap = {}
        answer = 0

        while p2 < len(s):
            c = s[p2]
            p2 += 1
            if c not in charMap:
                charMap[c] = 0
            charMap[c] += 1

            if len(charMap) <= k:
                answer = max(answer, p2-p1)
                continue 
            
            while len(charMap) > k:
                cDel = s[p1]
                p1 += 1
                charMap[cDel] -= 1
                if charMap[cDel] == 0:
                    del charMap[cDel]

        return answer