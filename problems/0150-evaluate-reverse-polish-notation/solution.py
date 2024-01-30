class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b)
        }

        for token in tokens:
            if token not in ops: stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[token](b, a))
        
        return round(stack.pop())
