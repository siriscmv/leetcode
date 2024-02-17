class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap, l = [], len(heights)

        for i in range(l - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)

                if len(heap) > ladders: bricks -= heapq.heappop(heap)
                if bricks < 0: return i
        return l - 1
