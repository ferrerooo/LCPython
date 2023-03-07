class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        dict1 = {}
        for n1 in nums1:
            if n1 not in dict1:
                dict1[n1] = 0
            dict1[n1] += 1
        
        for n2 in nums2:
            if n2 not in dict1:
                pass
            else:
                dict1[n2] -= 1
                answer.append(n2)
                if dict1[n2] == 0:
                    del dict1[n2]
        
        return answer