class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[src] += 1
            adj[dst].append(src)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        output = []
        while q:
            node = q.popleft()
            output.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(output) != numCourses:
            return []
        return output