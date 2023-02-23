# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peakIndex = self.findPeak(mountain_arr)
        answer = self.findFromLeft(target, mountain_arr, peakIndex)
        if answer != -1:
            return answer
        
        return self.findFromRight(target, mountain_arr, peakIndex)
    
    def findFromLeft(self, target, mountain_arr, peakIndex):
        p1 = 0
        p2 = peakIndex
        while p1 <= p2:
            mid = p1+ (p2-p1)//2
            midVal = mountain_arr.get(mid)
            if midVal == target:
                return mid
            elif midVal > target:
                p2 = mid-1
            else:
                p1 = mid+1
        return -1

    def findFromRight(self, target, mountain_arr, peakIndex):
        p1 = peakIndex
        p2 = mountain_arr.length()-1
        while p1 <= p2:
            mid = p1+ (p2-p1)//2
            midVal = mountain_arr.get(mid)
            if midVal == target:
                return mid
            elif midVal > target:
                p1 = mid+1
            else:
                p2 = mid-1
        return -1
    
    def findPeak(self, mountain_arr):
        p1 = 1
        p2 = mountain_arr.length()-2
        
        while (p1 <= p2):
            
            mid = p1 + (p2-p1)//2
            midVal = mountain_arr.get(mid)
            if midVal > mountain_arr.get(mid-1) and midVal > mountain_arr.get(mid+1):
                return mid
            
            if midVal < mountain_arr.get(mid-1) and midVal > mountain_arr.get(mid+1):
                p2 = mid-1
            else:
                p1 = mid+1
        
        return -1

