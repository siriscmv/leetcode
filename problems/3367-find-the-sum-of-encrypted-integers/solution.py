class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def enc(num):
            return int(str(max(map(int, list(str(num))))) * len(str(num)))
        
        ans = 0
        for n in nums:
            ans += enc(n)
            
        return ans
        
