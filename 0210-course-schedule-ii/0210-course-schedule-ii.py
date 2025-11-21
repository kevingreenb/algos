class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        g = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        ans = []
        seen = 0

        for course, prereq in prerequisites:
            g[prereq].append(course)
            indegree[course] += 1

        for i, val in enumerate(indegree):
            if val == 0:
                q.append(i)
        
        while q:
            current = q.popleft()
            ans.append(current)
            seen += 1
            for n in g[current]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        return ans if seen == numCourses else []