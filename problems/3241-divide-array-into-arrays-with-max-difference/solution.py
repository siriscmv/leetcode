class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            a, b, c = nums[i:i+3]
            if not(b-a <= k and c-b <= k and c-a <= k): return []
            ans.append([a, b, c])
        return ans
