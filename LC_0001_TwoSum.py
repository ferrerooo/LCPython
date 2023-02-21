class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        dict = {}
        for index, val in enumerate(nums):
            x2 = target - val
            if x2 in dict:
                result = [dict[x2], index]
                break
            else:
                dict[val] = index
        
        return result