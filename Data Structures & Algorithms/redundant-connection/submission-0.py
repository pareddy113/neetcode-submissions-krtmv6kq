class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(i, j):
            findI, findJ = find(i), find(j)

            if findI == findJ:
                return False
            
            if rank[findI] > rank[findJ]:
                par[findJ] = findI
                rank[findI] += rank[findJ]
            else:
                par[findI] = findJ
                rank[findJ] += rank[findI]
            return True

        for i,j in edges:
            if not union(i,j):
                return [i,j]

        