class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks: counts[task] += 1
        
        max_count = max(counts.values())        
        max_count_tasks = len([count for count in counts.values() if count == max_count])        
        intervals_needed = (max_count - 1) * (n + 1) + max_count_tasks
        
        return max(intervals_needed, len(tasks))
