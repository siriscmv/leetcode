from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()

        for k, s in enumerate(senate):
            if s == "R": R.append(k)
            elif s == "D": D.append(k)

        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d: R.append(r + len(senate))
            else: D.append(d + len(senate))

        return "Radiant" if R else "Dire"

