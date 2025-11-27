class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))

        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        
        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot != yroot:
                parent[yroot] = xroot
                return True
            return False
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]

        return []