from collections import defaultdict

class Solution:

    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0] * n
        x, y = min(x,y), max(x,y)
    
        for i in range(1, n):
            for j in range(i+1, n+1):
                l = min(j-i, abs(i-x) + 1 + abs(y-j))
                ans[l-1] += 1
                
        for i,n in enumerate(ans):
            ans[i] = n*2
        return ans
        
