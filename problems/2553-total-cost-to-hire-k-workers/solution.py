from heapq import heappush, heappop

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap, l, indices, cost = [], len(costs), set(), 0

        for i in range(candidates):
            for j in (i, l-1-i):
                if j not in indices:
                    indices.add(j)
                    heappush(heap, (costs[j], j))

        a, b = candidates-1, l-candidates
        for _ in range(k):
            val, ix = heappop(heap)
            cost += val

            if ix <= a:
                if a+1 in indices: continue
                a += 1
                if a >= l: continue
                
                indices.add(a)
                heappush(heap, (costs[a], a))
            else:
                if b-1 in indices: continue
                b -= 1
                if b < 0: continue
                
                indices.add(b)
                heappush(heap, (costs[b], b))

        return cost
