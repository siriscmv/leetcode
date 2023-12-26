class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            if num in mapping: mapping[num] +=1
            else: mapping[num] = 1
        
        return list(map(lambda x: x[0], sorted([(k, v) for k, v in mapping.items()], key=lambda x: x[1], reverse=True)[0:k]))
