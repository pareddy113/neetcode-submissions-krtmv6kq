class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = {i:[] for i in range(n)}

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        visited = set()

        def dfs(node, prev):

            if node in visited:
                return False

            visited.add(node)

            for i in adjList[node]:
                if i == prev:
                    continue
                dfs(i, node)
        
        size = 0
        for i in range(n):
            if len(visited) < n and i not in visited:
                size += 1
                dfs(i, -1)
                
        return size

        