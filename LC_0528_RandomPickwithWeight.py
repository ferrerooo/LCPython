class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        self.sum = 0
        for i in w:
            self.sum += i
            if len(self.arr) == 0:
                self.arr.append([0, i-1])
            else:
                item = self.arr[-1][1]
                self.arr.append([item+1, item+i])

    def pickIndex(self) -> int:
        rand = random.randint(0, self.sum-1)
        p1 = 0
        p2 = len(self.arr)-1
        answer = -1
        while p1 <= p2:
            mid = (p1+p2)//2
            if self.arr[mid][0] <= rand and self.arr[mid][1] >= rand:
                answer = mid
                break
            elif self.arr[mid][1] < rand:
                p1 = mid+1
            else:
                p2 = mid-1
        
        return answer
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()