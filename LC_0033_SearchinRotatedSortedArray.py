class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums)-1

        while p1 <= p2:

            mid = p1 + (p2-p1)//2

            if nums[mid] == target:
                return mid

            if nums[p1] <= nums[mid]:
                if nums[p1] <= target and target < nums[mid]:
                    p2 = mid-1
                else:
                    p1 = mid+1
            else:
                if nums[mid] < target and target <= nums[p2]:
                    p1 = mid+1
                else:
                    p2 = mid-1
        
        return -1
                