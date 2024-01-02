class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
      l, t = len(tickets), 0
      while True:
        for i, ticket in enumerate(tickets):
          if ticket == 0: continue
          t += 1
          tickets[i] -= 1
          if tickets[i] == 0 and i == k: return t
      return -1
