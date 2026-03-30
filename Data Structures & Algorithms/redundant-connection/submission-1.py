class Solution:
    '''
     When you try to union two nodes that already share the same root/parent (i.e., find(u) == find(v)), 
     that edge is the redundant one — because connecting two nodes that are already in the same component 
     is exactly what creates a cycle.
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
    
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            if root_u == root_v: # If they have the same root, this edge creates a cycle
                return [u, v]
            parent[root_u] = root_v
            

        # n = len(edges)
        # par = [i for i in range(n + 1)]
        # rank = [1] * (n + 1)

        # def find(node):
        #     while node != par[node]:
        #         par[node] = par[par[node]]
        #         node = par[node]
        #     return node
        
        # def union(i, j):
        #     findI, findJ = find(i), find(j)

        #     # If two parents equal, then any edge here creates a cycle
        #     if findI == findJ:
        #         return False
            
        #     if rank[findI] > rank[findJ]:
        #         par[findJ] = findI
        #         rank[findI] += rank[findJ]
        #     else:
        #         par[findI] = findJ
        #         rank[findJ] += rank[findI]
        #     return True

        # for i,j in edges:
        #     if not union(i,j):
        #         return [i,j]

        