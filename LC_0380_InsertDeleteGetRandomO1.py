from random import choice

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            listIndex = self.dict[val]
            valLast = self.list[-1]
            self.dict[valLast] = listIndex
            self.list[listIndex] = valLast
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()