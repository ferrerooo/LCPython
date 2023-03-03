class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            numSet.add(n)
        
        answer = 0

        for n in nums:

            if n not in numSet:
                continue
            
            numSet.remove(n)
            l = n-1
            leftCnt = 0
            r = n+1
            rightCnt = 0

            while True:
                if l in numSet:
                    leftCnt += 1
                    numSet.remove(l)
                    l = l-1
                else:
                    break
            
            while True:
                if r in numSet:
                    rightCnt += 1
                    numSet.remove(r)
                    r = r+1
                else:
                    break
            
            answer = max(answer, 1+leftCnt+rightCnt)
        
        return answer

                