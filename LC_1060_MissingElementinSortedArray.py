class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        p1 = 0
        p2 = len(nums)-1

        if p1 == p2:
            return nums[0]+k

        while p1 < p2 and p1+1 != p2:
            mid = (p1+p2)//2

            diff = (nums[mid] - nums[p1] + 1) - (mid-p1+1)

            if diff >= k:
                p2 = mid
            else:
                k = k - diff
                p1 = mid
        
        answer = nums[p1] + k
        if answer >= nums[p2]:
            answer += 1
        
        return answer