class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        gap = 10 ** 9
        answer = 10 ** 9
        n = len(nums)

        p1 = 0
        while p1 < n-2:
            p2 = p1+1
            p3 = n-1
            while p2 < p3:
                if nums[p1] + nums[p2] + nums[p3] == target:
                    return target
                elif nums[p1] + nums[p2] + nums[p3] > target:
                    if nums[p1] + nums[p2] + nums[p3] - target < gap:
                        gap = nums[p1] + nums[p2] + nums[p3] - target
                        answer = nums[p1] + nums[p2] + nums[p3]
                    p3 -= 1
                else:
                    if target - (nums[p1] + nums[p2] + nums[p3]) < gap:
                        gap = target - (nums[p1] + nums[p2] + nums[p3])
                        answer = nums[p1] + nums[p2] + nums[p3]
                    p2 += 1
            
            p1 += 1
        
        return answer