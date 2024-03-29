class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        for idx, val in items:
            heapq.heappush(d[idx], val)
            
            if len(d[idx]) > 5:
                heapq.heappop(d[idx])
        
        res = [[i, sum(d[i]) // 5] for i in sorted(d)]
        
        return res