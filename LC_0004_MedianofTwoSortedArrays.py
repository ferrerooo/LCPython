class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m: int = len(nums1)
        n: int = len(nums2)

        if (m+n)%2 == 1:
            a = self.dfs(nums1, nums2, (m+n)//2+1)
            if a == -1:
                a = self.dfs(nums2, nums1, (m+n)//2+1)
            return float(a)
        else:
            k1 = (m+n)//2
            k2 = (m+n)//2 + 1
            a = self.dfs(nums1, nums2, k1)
            if a == -1:
                a = self.dfs(nums2, nums1, k1)
            
            b = self.dfs(nums1, nums2, k2)
            if b== -1:
                b = self.dfs(nums2, nums1, k2)
            
            return (float(a)+b)/2
    
    def dfs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        m = len(nums1)
        n = len(nums2)

        p1 = 0
        p2 = m-1

        while p1 <= p2:


            mid = (p1 + (p2-p1)//2)
            arr2CheckIndex = (k-1-mid)


            #print("p1:",p1," p2:",p2, " k:", k, " mid:", mid, " arr2CheckIndex:", arr2CheckIndex)

            if arr2CheckIndex < 0:
                p2 = mid-1
                continue
            
            if arr2CheckIndex == 0:
                if n == 0 or nums1[mid] <= nums2[0]:
                    return nums1[mid]
                else:
                    p2 = mid-1
                continue
            
            if n < arr2CheckIndex:
                p1 = mid+1
                continue
            
            if n == arr2CheckIndex:
                if nums1[mid] >= nums2[arr2CheckIndex-1]:
                    return nums1[mid]
                else:
                    p1 = mid+1
                continue
            
            if nums1[mid] >= nums2[arr2CheckIndex-1] and nums1[mid] <= nums2[arr2CheckIndex]:
                return nums1[mid]
            elif nums1[mid] > nums2[arr2CheckIndex]:
                p2 = mid-1
            else:
                p1 = mid+1
        
        return -1