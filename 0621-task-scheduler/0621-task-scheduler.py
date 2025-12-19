class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_freq_counts = 0
        for v in counts.values():
            if v == max_freq:
                max_freq_counts += 1
        ans = (max_freq - 1) * (n + 1) + max_freq_counts
        return max(ans, len(tasks))