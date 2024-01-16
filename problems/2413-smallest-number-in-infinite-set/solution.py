class SmallestInfiniteSet:
    def __init__(self):
        self.set = set()
        self.max = 1

    def popSmallest(self) -> int:
        if not self.set:
            self.max += 1
            return self.max - 1
        
        ans = min(self.set)
        self.set.remove(ans)
        return ans

    def addBack(self, num: int) -> None:
        if num < self.max: self.set.add(num)
