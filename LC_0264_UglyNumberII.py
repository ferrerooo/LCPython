class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while len(arr) < n:
            nextNum = min(arr[i2]*2, arr[i3]*3, arr[i5]*5)
            arr.append(nextNum)
            if arr[i2]*2 == nextNum:
                i2 += 1
            if arr[i3]*3 == nextNum:
                i3 += 1
            if arr[i5]*5 == nextNum:
                i5 += 1
        
        return arr[-1]