class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, c = None, 0

        for num in nums:
            if not c: 
                ans = num
                c = 1
            elif ans == num: c += 1
            else: c -= 1
        
        return ans
