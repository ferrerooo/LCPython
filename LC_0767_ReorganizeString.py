from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) <= 1:
            return s

        count = Counter([c for c in s])
        d = []
        heapq.heapify(d)
        for k,v in count.items():
            heapq.heappush(d, (-1*v, k))
        
        answer = ''

        #print(d)

        while len(d) > 0:
            (cnt1, s1) = heapq.heappop(d)
            answer += s1
            cnt1 += 1
            (cnt2, s2) = (0, '')
            if len(d) > 0:
                (cnt2, s2) = heapq.heappop(d)
                answer += s2
                cnt2 += 1
            else:
                if cnt1 < 0:
                    return ''
            
            if cnt1 < 0:
                heapq.heappush(d, (cnt1, s1))
            
            if cnt2 < 0:
                heapq.heappush(d, (cnt2, s2))
            


        return answer
