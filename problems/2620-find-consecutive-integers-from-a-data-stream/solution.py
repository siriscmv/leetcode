class DataStream:
    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.curr = 0

    def consec(self, num: int) -> bool:
        if num == self.val: self.curr += 1
        else: self.curr = 0
        return self.curr >= self.k
