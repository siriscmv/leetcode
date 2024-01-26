class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, l = [], len(nums)
        nums.sort()

        for i in range(l-2):
            if nums[i] > 0: break
            if i and nums[i] == nums[i-1]: continue
            j, k = i + 1, l-1
            while j < k:
                a, b, c = nums[i], nums[j], nums[k]
                s = a + b + c
                if s >= 0: k -= 1
                if s <= 0: j += 1
                if not s: 
                    ans.append([a, b, c])
                    while nums[j] == nums[j-1] and j < k: j += 1
        
        return ans
