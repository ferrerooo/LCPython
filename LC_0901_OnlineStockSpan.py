class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1
        

    def next(self, price: int) -> int:
        answer = 0
        self.index += 1
        
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            self.stack.pop()
        
        if len(self.stack) == 0:
            answer = self.index + 1
        else:
            answer = self.index - self.stack[-1][1]
        
        self.stack.append((price, self.index))

        return answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)