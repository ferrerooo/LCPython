from sortedcontainers import SortedList, SortedDict

class MaxStack:

    def __init__(self):
        self.head = MaxStackNode(-1)
        self.tail = MaxStackNode(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dict = SortedDict()

    def push(self, x: int) -> None:
        node = MaxStackNode(x)
        lastNode = self.tail.pre
        lastNode.next = node
        node.pre = lastNode
        node.next = self.tail
        self.tail.pre = node

        if x not in self.dict:
            self.dict[x] = []
        self.dict[x].append(node)

    def pop(self) -> int:
        answer = self.tail.pre.val
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre
        self.dict[answer].pop()
        if len(self.dict[answer]) == 0:
            del self.dict[answer]
            #self.dict.remove(answer)
        
        return answer

    def top(self) -> int:
        return self.tail.pre.val

    def peekMax(self) -> int:
        return self.dict.peekitem()[1][-1].val

    def popMax(self) -> int:
        key = self.dict.peekitem()[0]
        node = self.dict.peekitem()[1].pop()
        answer = node.val
        if len(self.dict.peekitem()[1]) == 0:
            del self.dict[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        return answer


class MaxStackNode:
    def __init__(self, value):
        self.pre = None
        self.next = None
        self.val = value