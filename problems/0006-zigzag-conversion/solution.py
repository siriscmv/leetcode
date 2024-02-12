class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1: return s
        l, ans, skip = len(s), [], (n-1) * 2

        for i in range(n):
            for j in range(i, l, skip):
                ans.append(s[j])

                if i == 0 or i == n-1: continue
                if j+skip-i*2 < l: ans.append(s[j+skip-i*2])
        
        return "".join(ans)
