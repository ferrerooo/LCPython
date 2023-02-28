from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        answer = self.q1.pop(0)
        self.q1 = self.q2
        self.q2 = []
        return answer

    def top(self) -> int:

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        answer = self.q1[0]
        return answer

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    print(param_2)
    #param_3 = obj.pop()
    #param_4 = obj.pop()
    #param_5 = obj.empty()
