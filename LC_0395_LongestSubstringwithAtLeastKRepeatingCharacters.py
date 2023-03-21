class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

            answer = 0

            for distinctCnt in range(1, 27):
                p1 = 0
                p2 = 0
                charCntMap = {}
                while p2 < len(s):
                    if s[p2] not in charCntMap:
                        charCntMap[s[p2]] = 0
                    charCntMap[s[p2]] += 1

                    if len(charCntMap) == distinctCnt:
                        if self.getMinFreq(charCntMap) >= k:
                            answer = max(answer, p2-p1+1)
                    elif len(charCntMap) < distinctCnt:
                        pass
                    else:
                        while len(charCntMap) > distinctCnt:
                            charCntMap[s[p1]] -= 1
                            if charCntMap[s[p1]] == 0:
                                del charCntMap[s[p1]]
                            p1 += 1

                    p2 += 1
            
            return answer
        
    def getMinFreq(self, charCntMap):
        minFreq = 100000
        for v in charCntMap.values():
            minFreq = min(minFreq, v)
            
        return minFreq
                        
                    