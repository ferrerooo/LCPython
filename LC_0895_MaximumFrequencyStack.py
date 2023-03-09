class FreqStack:

    def __init__(self):
        self.valCntMap = {}
        self.cntValMap = {}
        self.maxCnt = 0
        

    def push(self, val: int) -> None:
        if val not in self.valCntMap:
            self.valCntMap[val] = 0
        
        self.valCntMap[val] += 1
        
        if self.valCntMap[val] not in self.cntValMap:
            self.cntValMap[self.valCntMap[val]] = []
        
        self.cntValMap[self.valCntMap[val]].append(val)

        self.maxCnt = max(self.maxCnt, self.valCntMap[val])

    def pop(self) -> int:

        val = self.cntValMap[self.maxCnt].pop()
        if len(self.cntValMap[self.maxCnt]) == 0:
            self.maxCnt -= 1
            del self.cntValMap[self.maxCnt + 1]
        
        self.valCntMap[val] -= 1
        
        if self.valCntMap[val] == 0:
            del self.valCntMap[val]
        
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()