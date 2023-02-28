from collections import deque

class HitCounter:

    def __init__(self):
        self.deq = deque()
        

    def hit(self, timestamp: int) -> None:
        if not ( self.deq and self.deq[-1][0]==timestamp ):
            self.deq.append( [timestamp,0] )

        self.deq[-1][1] += 1
        

    def getHits(self, timestamp: int) -> int:
        earliestTime = timestamp - 300
        count = 0

        for pair in reversed(self.deq):
            if pair[0] > earliestTime:
                count += pair[1]
        
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)