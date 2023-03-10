from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.keyTimeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyTimeMap:
            self.keyTimeMap[key] = SortedDict()
        self.keyTimeMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyTimeMap:
            return ""

        sortedMap = self.keyTimeMap[key]

        idx = sortedMap.bisect_right(timestamp)

        if idx == 0:
            return ""
        
        return sortedMap.peekitem(idx-1)[1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)