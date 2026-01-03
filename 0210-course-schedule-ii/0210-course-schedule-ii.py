class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()

        for c, p in prerequisites:
            indegree[c] += 1
            g[p].append(c)

        q = deque([i for i, v in enumerate(indegree) if v == 0])
        
        seen = 0
        ans = []
        while q:
            c = q.popleft()
            seen += 1
            ans.append(c)
            for e in g[c]:
                indegree[e] -= 1
                if indegree[e] == 0:
                    q.append(e)

        return ans if seen == numCourses else []
