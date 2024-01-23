class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans, l = 0, len(arr)

        def solve(i, curr):
            nonlocal ans
            if len(curr) != len(set(curr)): return
        
            ans = max(ans, len(curr))
            for j in range(i, l): solve(j+1, curr + arr[j])

        solve(0, "")
        return ans
