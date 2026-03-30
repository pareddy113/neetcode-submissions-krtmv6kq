class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            
            for nei in adj[node]:
                dfs(nei)

        res = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1
        return res