class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max, prev = 0, 0

        while True:
            try:
                start, fort_type = next(((i,f) for i,f in enumerate(forts[prev:], start=prev) if f == 1 or f == -1), (None, None))
                if start == None: return max 
                end = forts.index(-1, start) if fort_type == 1 else forts.index(1, start)
                if all(f == 0 for f in forts[start+1:end]) and end - start - 1 > max: max = end - start -1
                prev = start + 1
            except: return max
        
