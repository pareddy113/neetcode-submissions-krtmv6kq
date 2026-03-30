class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = {i:[] for i in range(n)}

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        visited = set()

        def dfs(node):
            visited.add(node)

            for i in adjList[node]:
                if i not in visited:
                    dfs(i)
        
        size = 0
        for i in range(n):
            if len(visited) < n and i not in visited:
                size += 1
                dfs(i)

        return size

        