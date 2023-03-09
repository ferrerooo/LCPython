class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap, -1 * num)
            return
        
        #if len(self.minHeap) == 0:
        #    heapq.heappush(self.minHeap, num)
        #    return
        
        if len(self.minHeap) == 0 or num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -1 * num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if abs(len(self.minHeap) - len(self.maxHeap)) <= 1:
            return
        
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*val)
        else:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)
        
        return


    def findMedian(self) -> float:

        #print(self.maxHeap)
        #print(self.minHeap)
        #print("-----")
        
        if len(self.minHeap) == len(self.maxHeap):
            v1 = self.minHeap[0]
            v2 = self.maxHeap[0] * -1
            return (v1+v2)/2
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0] * -1


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()