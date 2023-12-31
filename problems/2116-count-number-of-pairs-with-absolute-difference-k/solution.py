class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = len(nums)
        ans = 0

        for i, num in enumerate(nums):
            t1, t2 = num-k, num+k
            j=i+1
            while j<l: 
                if nums[j] == t1 or nums[j] == t2: ans += 1
                elif nums[j] > t1 and nums[j] > t2: break
                j += 1
            
        return ans
