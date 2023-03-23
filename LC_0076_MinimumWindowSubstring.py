from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        count = len(t)
        minlen = len(s)+1
        answer = ""

        p1 = 0
        p2 = 0

        while p2 < len(s):
            c = s[p2]
            p2 += 1

            if c in tmap:
                tmap[c] -= 1
                if tmap[c] >= 0:
                    count -= 1
            
            while count == 0:
                
                if p2-p1 < minlen:
                    minlen = p2-p1
                    answer = s[p1:p2]
                c1 = s[p1]
                p1 += 1
                if c1 in tmap:
                    tmap[c1] += 1
                    if tmap[c1] > 0:
                        count += 1
                #print(f'count:{count}, p1:{p1}, p2:{p2}, answer:{answer}')
            
            #print(f'count:{count}, p1:{p1}, p2:{p2}')

        return answer


