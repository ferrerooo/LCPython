class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        answer = 0
        p1 = 1
        p2 = max(ribbons)

        while p1 <= p2:
            mid = (p1+p2)//2
            cuts = 0
            for i in ribbons:
                cuts += i//mid
            
            if cuts < k:
                p2 = mid-1
            else:
                answer = max(answer, mid)
                p1 = mid+1
        
        return answer
        