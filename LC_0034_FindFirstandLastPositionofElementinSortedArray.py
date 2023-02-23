class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIndex = Solution.findLeft(nums, target)
        rightIndex = Solution.findRight(nums, target)
        return [leftIndex, rightIndex]
    
    def findLeft(nums, target) -> int:
        p1 = 0
        p2 = len(nums)-1
        while p1 <= p2:
            mid = p1 + (p2-p1)//2
            if nums[mid] > target:
                p2 = mid-1
            elif nums[mid] < target:
                p1 = mid+1
            else:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    p2 = mid-1
        
        return -1
    
    def findRight(nums, target) -> int:

        p1 = 0
        p2 = len(nums)-1
        while p1 <= p2:
            mid = p1 + (p2-p1)//2
            if nums[mid] > target:
                p2 = mid-1
            elif nums[mid] < target:
                p1 = mid+1
            else:
                if mid == len(nums)-1 or nums[mid+1] > target:
                    return mid
                else:
                    p1 = mid+1
        
        return -1

