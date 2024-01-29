class MyQueue:
    def __init__(self):
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        self.right.append(x)

    def pop(self) -> int:
        if self.left: return self.left.pop()

        temp = []
        while self.right: temp.append(self.right.pop())
        ans = temp.pop()
        while temp: self.right.append(temp.pop())
        return ans

    def peek(self) -> int:
        ans = self.pop()
        self.left.append(ans)

        return ans
        
    def empty(self) -> bool:
        return not(self.left or self.right)
