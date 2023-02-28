class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = []
        if len(v1) > 0:
            self.q.append(v1)
        if len(v2) > 0:
            self.q.append(v2)

    def next(self) -> int:
        cur = self.q.pop(0)
        answer = cur.pop(0)
        if len(cur) > 0:
            self.q.append(cur)
        return answer

    def hasNext(self) -> bool:
        return len(self.q) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())