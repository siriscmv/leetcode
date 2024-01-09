from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)
    
    def index(self, key: int, ts: int) -> int:
        return bisect_right(self.data[key], ts, key = lambda x: x[1])
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data: return ""
        d = self.data[key]
        i = self.index(key, timestamp)
        if i == len(d): i -= 1
        if d[i][1] > timestamp: i -= 1
        if i < 0: return ""
        return d[i][0]
