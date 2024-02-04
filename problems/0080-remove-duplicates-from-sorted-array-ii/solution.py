class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, seen, curr = 1, False, nums[0]

        while i < len(nums):
            if nums[i] == curr:
                if not seen: seen = True
                else: 
                    del nums[i]
                    continue
            else:
                curr = nums[i]
                seen = False
            
            i += 1
        
        return len(nums)
