class Solution:
    def decodeString(self, s: str) -> str:
        reading, curr, stack, ans = 0, 0, [], []

        for ch in s:
            if ch.isdigit() and not reading: curr = curr * 10 + int(ch)
            elif ch == '[': 
                reading += 1
                if reading > 1: stack.append(ch)
            elif ch == ']':
                reading -= 1
                if reading: stack.append(ch)
                else:
                    ix = next((i for i, val in enumerate(stack) if val.isdigit()), -1)
                    if ix == -1: ans.append("".join(stack) * curr)
                    else:
                        a, b = stack[:ix], stack[ix:]
                        ans.append(("".join(a) + self.decodeString("".join(b))) * curr)
                    reading, curr, stack = 0, 0, []
            elif reading: stack.append(ch)
            else: ans.append(ch)
        
        return "".join(ans)
