class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        p1 = min(nums)
        p2 = max(nums)
        gap = 1E-5

        while p2 - p1 >= gap:
            mid = (p1+p2)/2
            b = self.hasLargerAvgValue(nums, mid, k)
            print(b)
            if b:
                p1 = mid
            else:
                p2 = mid
            

        return p1
    
    def hasLargerAvgValue(self, nums, mid, k) -> bool:
        arr = list(map(lambda x: x-mid, nums))
        sum = 0
        for i in range(k):
            sum += arr[i]
        
        if sum >= 0:
            return True
        
        index = k
        minPreSum = 0
        preSum = 0

        while index < len(arr):
            sum += arr[index]
            preSum += arr[index-k]
            minPreSum = min(minPreSum, preSum)
            if sum - minPreSum >= 0:
                return True
            index += 1
        
        return False

