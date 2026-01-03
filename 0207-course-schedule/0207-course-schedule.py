class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()

        for c, p in prerequisites:
            indegree[c] += 1
            g[p].append(c)
        
        q = deque([ i for i, v in enumerate(indegree) if v == 0])
        seen = 0
        while q:
            c = q.popleft()
            seen += 1
            for e in g[c]:
                indegree[e] -= 1
                if indegree[e] == 0:
                    q.append(e)

        return seen == numCourses
