class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        answer = []
        p1 = 0
        
        while p1 < len(nums)-2:
            p2 = p1 + 1
            p3 = len(nums) - 1
            while p2 < p3:
                if nums[p1] + nums[p2] + nums[p3] == 0:
                    answer.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1
                    p3 -= 1
                    while p2 < len(nums) and nums[p2] == nums[p2-1]:
                        p2 += 1
                    while p3 > p1 and nums[p3] == nums[p3+1]:
                        p3 -= 1
                elif nums[p1] + nums[p2] + nums[p3] > 0:
                    p3 -= 1
                else:
                    p2 += 1
            
            p1 += 1
            while p1 < len(nums)-2 and nums[p1] == nums[p1-1]:
                p1 += 1
            
        return answer