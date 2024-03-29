class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = []
        self.sum = 0
        

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum -= self.q.pop(0)
        return self.sum/len(self.q)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)