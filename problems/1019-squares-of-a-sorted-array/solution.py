class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans, q = [], deque()
        i, l = 0, len(nums)

        while i < l:
            n = nums[i]

            if n < 0: 
                q.appendleft(-n)
                i += 1
            elif q and q[0] <= n: 
                ans.append(q.popleft() ** 2)
            else: 
                ans.append(n ** 2)
                i += 1
        
        while q: ans.append(q.popleft() ** 2)
        return ans
