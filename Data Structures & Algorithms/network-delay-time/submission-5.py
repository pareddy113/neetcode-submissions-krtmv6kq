import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        
        weights = [ float('inf') for _ in range(n + 1)] 

        adj_list = defaultdict(list)
        
        for s, d, c in times:
            adj_list[s].append((d, c))

        heap = []
        visited = set()
        weights[k] = 0

        heapq.heappush(heap, (k, 0))
        visited.add(k)

        print(adj_list)
        while heap:
            s,c = heapq.heappop(heap)

            for d, cost in adj_list[s]:
                nc = c + cost
                print(nc)
                if nc < weights[d]:
                    weights[d] = nc
                    heapq.heappush(heap, (d, nc))
                    visited.add(d)
        
        print(weights)
        return max(weights[1:]) if max(weights[1:]) < float('inf') else -1
        

