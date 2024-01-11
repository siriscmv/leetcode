from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count += 1

        while t - self.queue[0] > 3000:
            self.queue.popleft()
            self.count -= 1

        return self.count
