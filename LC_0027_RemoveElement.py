class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p2] == val:
                p2 += 1
            else:
                swap(nums, p1, p2)
                p1 += 1
                p2 += 1
        
        return p1
    
def swap(nums: List[int], p1: int, p2: int):
    temp = nums[p1]
    nums[p1] = nums[p2]
    nums[p2] = temp

