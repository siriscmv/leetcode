class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s, d = min(start, destination), max(start, destination)

        a1 = sum(distance[s:d])
        a2 = sum(distance[d:]) + sum(distance[:s])
        
        return min(a1, a2)
