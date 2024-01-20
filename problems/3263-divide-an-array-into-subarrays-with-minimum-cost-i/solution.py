class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nn = sorted(enumerate(nums), key = lambda x: x[1])
        indices = nn[:3]        
        if any([i == 0 for i,_ in indices]): return indices[0][1]  + indices[1][1] + indices[2][1]
        return nums[0] + indices[0][1] + indices[1][1]
