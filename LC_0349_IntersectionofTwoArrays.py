class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer = []
        for n2 in set2:
            if n2 in set1:
                answer.append(n2)
        
        return answer