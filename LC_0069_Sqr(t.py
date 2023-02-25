class Solution:
    def mySqrt(self, x: int) -> int:
        
        p1 = 0
        p2 = x
        answer = -1

        while p1 <= p2:
            mid = (p1+p2)//2
            if mid**2 <= x and (mid+1)**2 > x:
                answer = mid
                break
            elif (mid+1)**2 <= x:
                p1 = mid+1
            else:
                p2 = mid-1
        
        return answer