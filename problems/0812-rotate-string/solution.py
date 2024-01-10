class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)
        if len(goal) != l: return False

        indices = [i for i, ch in enumerate(s) if ch == goal[0]]
        for x in indices:
            if all([s[(x+i) % l] == goal[i] for i in range(l)]): return True

        return False
        
