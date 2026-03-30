# For undirected graphs, only visited set is enough as an edge connects both.
'''
    In an Undirected Graph, the rules are much stricter. If you are at node U and you see a neighbor V
    that is already in your visited set, there are only two possibilities:
        - V is the parent (the node you just came from)
        - V is any other node you've seen before.
        
    If it is #2, it is guaranteed to be a cycle. It doesn't matter if V is currently 
    in the recursion stack or if it was finished 10 minutes ago. 
    In an undirected graph, any "shortcut" back to a previously seen 
    node (that isn't your parent) creates a loop.
'''

# For directed graphs, visiting and visited sets are required to detect a cycle as edges are directed.
'''
    When DFS goes A-> B -> D, D is marked as visited. When DFS later goes A -> C -> D, 
    it sees D is already visited. But there is no cycle! 
    To find a cycle, you need to know if $D$ is currently "above you" in the active recursion stack. 
    That's why you need the visiting set.
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):

            while (node != par[node]):
                par[node] = par[par[node]]
                node = par[node]
            return node

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return 0
            
            if rank[r1] > rank[r2]:
                par[r2] = r1
                rank[r1] += rank[r2]
            else:
                par[r1] = r2
                rank[r2] += rank[r1]
            return 1
        
        res = n
        for i, j in edges:
            res -= union(i,j)
        return res