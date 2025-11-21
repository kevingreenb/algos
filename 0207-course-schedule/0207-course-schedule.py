class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = defaultdict(list)
        indegree = [0]*numCourses
        q = deque()
        seen = 0

        for course, prereq in prerequisites:
            g[prereq].append(course)
            indegree[course] += 1
        
        for course, val in enumerate(indegree):
            if val == 0:
                q.append(course)

        while q:
            current = q.popleft()
            seen += 1
            for c in g[current]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return seen == numCourses

        