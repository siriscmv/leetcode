from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        indices = defaultdict(int)
        for (a, b) in rectangles: indices[a/b] += 1
        
        return sum([i * (i-1) // 2 for i in indices.values()])
