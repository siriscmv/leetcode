class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        marked = set()
        marked_sum = 0
        total_sum = sum(nums)
        ans = []
        
        sorted_nums = deque(sorted(enumerate(nums), key=lambda x: (x[1], x[0])))
        
        for (i, k) in queries:
            if i not in marked:
                marked.add(i)
                marked_sum += nums[i]
            
            for _ in range(k):
                while sorted_nums and sorted_nums[0][0] in marked: sorted_nums.popleft()
                
                if sorted_nums: 
                    a, b = sorted_nums.popleft()
                    marked.add(a)
                    marked_sum += b
            
            ans.append(total_sum - marked_sum)
        
        return ans
        
