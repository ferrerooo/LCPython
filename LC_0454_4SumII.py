class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        map12 = {}
        map34 = {}
        answer = 0

        for i in nums1:
            for j in nums2:
                k = i + j
                if k not in map12:
                    map12[k] = 0
                map12[k] += 1
        
        for i in nums3:
            for j in nums4:
                k = i + j
                if k not in map34:
                    map34[k] = 0
                map34[k] += 1
        
        for k in map12.keys():
            p = 0 - k
            if p in map34:
                answer += map12[k] * map34[p]
        
        return answer