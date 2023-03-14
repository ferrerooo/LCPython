class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        left = [i for i in range(len(arr))]
        right = [i for i in range(len(arr))]
        p1 = 0
        while p1 < len(arr):
            if p1 == 0:
                left[p1] = -1
                p1 += 1
                continue
            
            index = p1-1
            while arr[p1] <= arr[index]:
                index = left[index]
                if index == -1:
                    break
                
            left[p1] = index
            p1 += 1
        
        p2 = len(arr) - 1
        while p2 >= 0:
            if p2 == len(arr) - 1:
                right[p2] = len(arr)
                p2 -= 1
                continue
            
            index = p2 + 1
            while arr[p2] < arr[index]:
                index = right[index]
                if index == len(arr):
                    break
            right[p2] = index
            p2 -= 1
        
        answer = 0

        for i in range(len(arr)):
            answer = ((arr[i] * (i - left[i]) * (right[i] - i))%MOD + answer)%MOD

        return answer


        