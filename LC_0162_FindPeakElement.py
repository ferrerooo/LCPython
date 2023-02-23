class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        p1 = 1
        p2 = len(nums)-2

        while p1 <= p2:
            
            mid = p1 + (p2-p1)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                p2 = mid-1
                continue
            
            if nums[mid]<=nums[mid-1] and nums[mid]>=nums[mid+1]:
                p2 = mid-1
            else:
                p1 = mid+1
        
        return -1