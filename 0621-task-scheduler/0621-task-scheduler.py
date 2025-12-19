class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        counts = Counter(tasks)
        max_freq = max(counts.values())
        
        # Count how many tasks have that maximum frequency
        max_freq_count = 0
        for task in counts:
            if counts[task] == max_freq:
                max_freq_count += 1
                
        # Calculate the formulaic result
        ans = (max_freq - 1) * (n + 1) + max_freq_count
        
        # If we have many tasks and few idle slots, the length
        # could actually be longer than the formula (no idle time).
        # In that case, the answer is just the total number of tasks.
        return max(ans, len(tasks))