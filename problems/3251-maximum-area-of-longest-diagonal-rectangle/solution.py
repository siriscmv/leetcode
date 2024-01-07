class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = max([a*a + b*b for a,b in dimensions])
        
        return max([a*b for a, b in dimensions if a*a + b*b == max_area])
        
