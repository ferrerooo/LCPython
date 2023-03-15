class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-1] * len(nums)
        stack = []  # saving indexes

        for i, v in enumerate(nums):
            while len(stack) > 0 and v > nums[stack[-1]]:
                answer[stack.pop()] = v
            stack.append(i)
        
        for i, v in enumerate(nums):
            while len(stack) > 0 and v > nums[stack[-1]]:
                answer[stack.pop()] = v
            
        return answer

