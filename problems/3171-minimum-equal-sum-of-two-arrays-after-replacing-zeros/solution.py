class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sa, sb, a, b = 0, 0, 0, 0
        for num in nums1:
            if num == 0: a += 1
            sa += num
        for num in nums2:
            if num == 0: b += 1
            sb += num
        
        if a and b: return max(sa + a, sb + b)
        if a: return sb if sb >= sa + a else -1
        if b: return sa if sa >= sb + b else -1
        return sa if sa == sb else -1
