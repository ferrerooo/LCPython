class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        answer = []
        p1 = 0

        while p1 < n-3:
            p2 = p1 + 1
            while p2 < n-2:
                p3 = p2+1
                p4 = n-1

                while p3 < p4:
                    if nums[p1] + nums[p2] + nums[p3] + nums[p4] == target:
                        answer.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        p3 += 1
                        p4 -= 1
                        while p3<n and nums[p3] == nums[p3-1]:
                            p3 += 1
                        while p4>p2 and nums[p4] == nums[p4+1]:
                            p4 -= 1
                    elif nums[p1] + nums[p2] + nums[p3] + nums[p4] > target:
                        p4 -= 1
                    else:
                        p3 += 1
                
                p2 += 1
                while p2 < n-2 and nums[p2] == nums[p2-1]:
                    p2 += 1
            
            p1 += 1
            while p1 < n-3 and nums[p1] == nums[p1-1]:
                p1 += 1
        
        return answer