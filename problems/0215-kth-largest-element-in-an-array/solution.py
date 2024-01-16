from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapify(heap)
        
        for _ in range(k-1): heappop(heap)
        return -heappop(heap)
