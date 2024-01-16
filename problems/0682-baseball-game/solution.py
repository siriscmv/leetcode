class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.isdigit() or op[0] == "-" and op[1:].isdigit(): stack.append(int(op))
            elif op == "+": stack.append(stack[-1] + stack[-2])
            elif op == "D": stack.append(stack[-1] * 2)
            elif op == "C": stack.pop()
        
        return sum(stack)
