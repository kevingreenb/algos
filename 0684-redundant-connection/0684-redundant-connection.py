class Solution(object):
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1)) 

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x]) 
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                return True
            else:
                return False 

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []