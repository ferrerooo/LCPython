class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p2] == 0:
                p2 += 1
            else:
                temp = nums[p2]
                nums[p2] = nums[p1]
                nums[p1] = temp
                p1 += 1
                p2 += 1
        
        return