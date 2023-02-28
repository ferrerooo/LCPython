class FirstUnique:

    def __init__(self, nums: List[int]):
        self.numMap = {}
        self.q = []
        for i in nums:
            self.q.append(i)
            if i in self.numMap:
                self.numMap[i] = self.numMap[i] + 1
            else:
                self.numMap[i] = 1
        

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.numMap[self.q[0]] > 1:
            self.q.pop(0)
        
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value: int) -> None:
        if value in self.numMap:
            self.numMap[value] = self.numMap[value] + 1
        else:
            self.numMap[value] = 1
            self.q.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)