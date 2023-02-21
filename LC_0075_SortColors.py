class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        p3 = len(nums) - 1

        while p2 <= p3:

            if nums[p2] == 1:
                p2 += 1
            elif nums[p2] == 0:
                swap(nums, p1, p2)
                p1 += 1
                p2 += 1
            else:
                swap(nums, p2, p3)
                p3 -= 1

def swap(nums: List[int], a: int, b: int):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp