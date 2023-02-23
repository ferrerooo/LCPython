# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        p1 = 1
        p2 = n
        while p1 <= p2:
            mid = p1 + (p2-p1)//2
            if not isBadVersion(mid):
                p1 = mid+1
            else:
                if mid == 1 or not isBadVersion(mid-1):
                    return mid
                else:
                    p2 = mid-1
        
        return -1