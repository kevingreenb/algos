class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = [0] * numCourses

        for c, p in prerequisites:
            g[p].append(c)
            indegree[c] += 1

        q = deque([c for c, v in enumerate(indegree) if v == 0])
        seen = 0
        while q:
            c = q.popleft()
            seen += 1
            for nei in g[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return seen == numCourses