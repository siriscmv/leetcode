class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_total = 0
        for num in nums: xor_total ^= num
        target_xor = xor_total ^ k
        
        operations = 0
        while target_xor > 0:
            operations += target_xor & 1
            target_xor >>= 1
        return operations
        
