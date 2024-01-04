class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
      return len(rooms) == len(self.dfs(0, rooms, set()))
    
    def dfs(self, start, rooms, path):
      if start in path: return
      path.add(start)
      for room in rooms[start]: self.dfs(room, rooms, path)
      return path
