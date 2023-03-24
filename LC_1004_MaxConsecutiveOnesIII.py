class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1 = 0
        p2 = 0
        cnt0 = 0
        cnt1 = 0
        answer = 0

        while p2 < len(nums):
            if nums[p2] == 1:
                cnt1 += 1
            else:
                cnt0 += 1
            
            p2 += 1

            if cnt0 <= k:
                answer = max(answer, p2 - p1)
            else:
                while cnt0 > k:
                    if nums[p1] == 1:
                        cnt1 -= 1
                    else:
                        cnt0 -= 1
                    p1 += 1
        
        return answer