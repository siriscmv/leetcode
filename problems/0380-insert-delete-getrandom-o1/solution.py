class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.list = list()

    def insert(self, val: int) -> bool:
        if val in self.map: return False

        self.list.append(val)
        self.map[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False

        i = self.map[val]
        del self.map[val]
        self.list[i] = self.list[-1]
        if i < len(self.list) - 1: self.map[self.list[-1]] = i
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.list)
