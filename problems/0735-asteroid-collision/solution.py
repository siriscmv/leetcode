class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack: 
                stack.append(a)
                continue
            prev = stack[-1]
            if not(prev>0 and a<0): stack.append(a)
            else:
                if abs(a) < abs(prev): pass
                elif abs(a) == abs(prev): stack.pop()
                else:
                    stack.append(a)
                    while len(stack) > 1: 
                        b, a = stack[-2], stack[-1]
                        if not(b>0 and a<0): break
                        if abs(b) <= abs(a): del stack[-2]
                        if abs(b) >= abs(a): del stack[-1]
        
        return stack
