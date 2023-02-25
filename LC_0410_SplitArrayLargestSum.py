class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        p1 = 0
        p2 = sum(nums)
        answer = p2

        while p1 <= p2:
            mid = (p1+p2)//2
            groups = 0
            cur = 0
            index = 0
            while index < len(nums):
                if nums[index] > mid:
                    groups = 2000
                    break
                if cur + nums[index] <= mid:
                    cur += nums[index]
                    index += 1
                else:
                    groups += 1
                    cur = 0

            if cur > 0:
                groups += 1
            
            print(f'p1={p1}, p2={p2}, mid={mid}, groups={groups}')

            if groups > k:
                p1 = mid+1
            else:
                answer = min(answer, mid)
                p2 = mid-1
        
        return answer


