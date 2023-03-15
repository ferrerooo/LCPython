class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        for n in nums2:
            while len(stack) > 0 and n > stack[-1]:
                d[stack.pop()] = n
            stack.append(n)
        
        answer = []
        for n in nums1:
            if n in d:
                answer.append(d[n])
            else:
                answer.append(-1)
            
        return answer