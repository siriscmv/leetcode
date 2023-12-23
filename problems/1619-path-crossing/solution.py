class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = [(0, 0)]
        for p in path:
            prev = coords[-1]

            if p == "N": next = (prev[0], prev[1]+1)
            elif p == "S": next = (prev[0], prev[1]-1)
            elif p == "E": next = (prev[0]+1, prev[1])
            elif p == "W": next = (prev[0]-1, prev[1])

            if next in coords: return True
            else: coords.append(next)
        return False
        
