class StockSpanner:
    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, prev = self.stack.pop()
            span += prev

        self.stack.append((price, span))
        return span
