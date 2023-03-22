class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        p2 = 0
        charmap = {}
        answer = 0

        while p2 < len(s):

            c = s[p2]
            p2 += 1
            
            if c not in charmap:
                charmap[c] = 0
            charmap[c] += 1

            if self.getMinorityCharCnt(charmap) <= k:
                answer = max(answer, p2-p1)
                continue
            
            while self.getMinorityCharCnt(charmap) > k:
                cdel = s[p1]
                p1 += 1
                charmap[cdel] -= 1
                if charmap[cdel] == 0:
                    del charmap[cdel]
        
        return answer
    
    def getMinorityCharCnt(self, charmap):
        total = 0
        maxcnt = 0
        for v in charmap.values():
            total += v
            maxcnt = max(maxcnt, v)
        return total - maxcnt