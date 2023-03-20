class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1

        def swap(nums, p1, p2):
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp

        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                swap(nums, p1+1, p2)
                p2 += 1
                p1 += 1

        return p1+1