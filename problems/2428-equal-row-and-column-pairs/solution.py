from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, hashmap = len(grid), defaultdict(lambda: [set(), set()])

        for i in range(n): 
            nums = map(str, grid[i])
            hashmap["|".join(nums)][0].add(i)

        for i in range(n):
            nums = [str(grid[j][i]) for j in range(n)]
            hashmap["|".join(nums)][1].add(i)
        
        ans = 0
        for k in hashmap:
            a, b = hashmap[k]
            ans += len(a) * len(b)
        return ans
