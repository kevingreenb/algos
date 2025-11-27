class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = [0]*numCourses
        q = deque()
        seen = 0
        ans = []

        for c, p in prerequisites:
            indegree[c] += 1
            g[p].append(c)

        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)
        
        while q:
            current = q.popleft()
            seen += 1
            ans.append(current)
            for c in g[current]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return ans if seen == numCourses else []