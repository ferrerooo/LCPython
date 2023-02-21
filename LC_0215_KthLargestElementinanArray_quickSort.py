class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.dfs(nums, 0, len(nums)-1, len(nums)-k+1)
    
    def dfs(self, nums, p1, p2, k) -> int:
        #print("k is ", k)
        if p1 == p2:
            return nums[p1]
        
        a = p1
        b = p1
        c = p2
        pivot = nums[random.randint(p1, p2)]

        while b <= c:
            if nums[b] == pivot:
                b += 1
            elif nums[b] < pivot:
                self.swap(nums, a, b)
                a += 1
                b += 1
            else:
                self.swap(nums, b, c)
                c -= 1
        
        #print(nums)

        if k == c-p1+1:
            return nums[c]
        
        #print("c:", c, "p1:",p1 , "p2:", p2)
        if c-p1+1 > k:
            #print("ONE: left:", p1, " right:", c-1, " k:",k, " nextK:", k)
            return self.dfs(nums, p1, c-1, k)
        else:
            #print("TWO: left:", c+1, " right:", p2, " k:",k, " nextK:", k-c-1)
            return self.dfs(nums, c+1, p2, k-c-1+p1)

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
