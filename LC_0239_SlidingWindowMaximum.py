from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        answer = []
        for i in range(k):
            val = nums[i]
            while len(q) > 0 and val > q[-1][0]:
                q.pop()
            q.append((val, i))
        
        answer.append(q[0][0])

        for i in range(1, len(nums) - k + 1):
            idx1 = i - 1
            idx2 = i + k - 1
            val1 = nums[idx1]
            val2 = nums[idx2]
            if q[0][1] == idx1:
                q.popleft()
            while len(q) > 0 and val2 > q[-1][0]:
                q.pop()
            q.append((val2, idx2))
            answer.append(q[0][0])
        
        return answer
            

        
