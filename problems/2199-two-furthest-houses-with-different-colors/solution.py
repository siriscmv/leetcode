class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        i, l = 0, len(colors)
        while i<l-1:
            j=l-1
            if j-1<ans: return ans # Early exit
            while j>i and colors[j] == colors[i]: j -= 1
            if j<i: continue
            ans = max(ans, j-i)
            i += 1
        return ans 
