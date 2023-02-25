class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        p1 = 0
        p2 = len(nums)-1
        answer = -1

        while p1 <= p2:

            mid = (p1+p2)//2

            if mid == 0 or mid == len(nums)-1:
                answer = mid
                break
            
            if nums[mid] == nums[mid-1]:
                if (mid-p1+1)%2 == 0:
                    p1 = mid+1
                else:
                    p2 = mid
            elif nums[mid] == nums[mid+1]:
                if (p2-mid+1)%2 == 0:
                    p2 = mid-1
                else:
                    p1 = mid
            else:
                answer = mid
                break
        
        return nums[answer]