class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prev, rl = 0, []
        for shift in shifts[::-1]: 
            rl.append(shift+prev)
            prev += shift
        
        rl, ans = rl[::-1], list(s)
        for i, shift in enumerate(rl):
            ans[i] = chr(ord('a') + ((ord(ans[i]) - ord('a') + shift) % 26))
        return "".join(ans)
