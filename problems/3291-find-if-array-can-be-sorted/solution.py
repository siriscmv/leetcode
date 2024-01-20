class Solution:
    def count_set_bits(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def canSortArray(self, nums: List[int]) -> bool:
        swapped = False
        bits = {}
        
        for n in nums: bits[n] = self.count_set_bits(n)
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    if bits[nums[j]] != bits[nums[j+1]]: return False
                    swapped = True
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            
            if not swapped: break
        
        return True
        
