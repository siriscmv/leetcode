from heapq import heappush, heappop

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        heap = []
        counts = {}

        for ch in 'abcdefghijklmnopqrstuvwxyz': counts[ch] = 0
        
        for ch in s:
            if ch != '?': counts[ch] += 1
        
        for ch in counts: heappush(heap, (counts[ch], ch))
        
        possible_ans = []
        
        for _ in range(s.count('?')):
            n, c = heappop(heap)
            possible_ans.append(c)
            heappush(heap, (n+1, c))
            
        possible_ans = deque(sorted(possible_ans))
        ans = list(s)

        for i in range(len(ans)):
            if ans[i] == '?': ans[i] = possible_ans.popleft()
        
        return "".join(ans)
