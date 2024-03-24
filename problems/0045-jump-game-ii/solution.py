class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        j = n-1

        while j:
            for i in range(j):
                if i + nums[i] >= j:
                    ans += 1
                    j = i
                    break
        
        return ans
