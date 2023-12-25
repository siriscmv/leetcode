class Solution:
        def run(self, input: list[int]) -> bool:
            return self.validPartition(input)
        
        dp = {}
        def validPartition(self, nums: list[int]) -> bool:
            global dp
            dp = {}
            
            return self.solve(nums, 0)

        def solve(self, nums: list[int], i) -> bool:
            l = len(nums) - i
            if l == 0: return True
            if i in dp: return dp[i]

            res = False
            if l >= 2 and nums[i] == nums[i+1]:
                res = self.solve(nums, i+2)

            if l >= 3 and ((nums[i] == nums[i+1] and nums[i+1] == nums[i+2]) or (nums[i+1] == nums[i+0] + 1 and nums[i+2] == nums[i+1] + 1)):
                res = res or self.solve(nums, i+3)

            dp[i] = res
            return res
