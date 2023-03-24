class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        p1 = 0
        p2 = 0
        answer = -1
        target = sum(nums) - x
        cur = 0

        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)

        #print(f'target:{target}')

        while p2 < len(nums):
            cur += nums[p2]
            p2 += 1

            if cur < target:
                #print(f'111- p1:{p1}, p2:{p2}, subarray:{nums[p1:p2]}, cur:{cur}, target:{target}')
                pass
            elif cur == target:
                answer = max(answer, p2-p1)
                cur -= nums[p1]
                p1 += 1
                #print(f'2nd- p1:{p1}, p2:{p2}, subarray:{nums[p1:p2]}, cur:{cur}, target:{target}')
            else:
                #print(f'333- p1:{p1}, p2:{p2}, subarray:{nums[p1:p2]}, cur:{cur}, target:{target}')
                while cur > target:
                    cur -= nums[p1]
                    p1 += 1
                if cur == target:
                    answer = max(answer, p2-p1)
                    cur -= nums[p1]
                    p1 += 1

        if answer == -1:
            return answer
        else:
            return len(nums) - answer
