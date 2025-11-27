class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)

        for n1, n2, w in times:
            g[n1].append((n2, w))

        dist = {}
        mq = [(0, k)]

        while mq:
            cost1, current = heapq.heappop(mq)

            if current in dist:
                continue

            dist[current] = cost1

            for nei, cost2 in g[current]:
                heapq.heappush(mq, (cost1+cost2, nei))
        
        return -1 if len(dist) != n else max(dist.values())

        