class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return list(map(lambda c: c+extraCandies >= m,  candies))
        
