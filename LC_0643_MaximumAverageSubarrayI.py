class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        current = 0
        
        for i in range(k):
            current += nums[i]
        
        answer = current

        for i in range(k, len(nums)):
            current -= nums[i-k]
            current += nums[i]
            answer = max(answer, current)
        
        return answer/k
