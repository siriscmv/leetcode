class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        m = {'+': lambda a, b: a+b, '-': lambda a, b: a-b, '*': lambda a, b: a*b, '/': lambda a, b: int(a/b)}
        for token in tokens:
            if token not in m: stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(m[token](b, a))
        return round(stack.pop())
