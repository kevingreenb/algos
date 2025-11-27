class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        g = defaultdict(list)
        visited = set([k])
        q = deque([(k, 0)])
        seen = 0
        ans = 0

        for n1, n2, c in times:
            g[n1].append((n2, c))

        while q:
            current, cost1 = q.popleft()
            seen += 1

            for nei, cost2 in g[current]:
                if nei not in visited:
                    new_cost = cost1+cost2
                    visited.add(nei)
                    q.append((nei, new_cost))
                    ans = max(ans, new_cost)
        
        return ans if seen == n else -1
        