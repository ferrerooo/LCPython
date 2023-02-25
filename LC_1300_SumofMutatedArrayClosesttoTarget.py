class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        p1 = 0
        p2 = max(arr)
        gap = 1000000000
        answer = 100000

        while p1 <= p2:
            mid = (p1+p2)//2
            sum = 0
            for i in arr:
                if i > mid:
                    sum += mid
                else:
                    sum += i
            
            if target == sum:
                return mid

            if abs(target - sum) < gap:
                gap = abs(target - sum)
                answer = mid
            elif abs(target - sum) == gap:
                answer = min(answer, mid)
            
            if target > sum:
                p1 = mid+1
            else:
                p2 = mid-1
        
        return answer

            
