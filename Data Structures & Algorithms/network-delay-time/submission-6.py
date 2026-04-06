import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        adjL = defaultdict(list)
        for s, t, c in times:
            adjL[s].append((t, c))

        # min heap: (cost, node)
        heap = [(0, k)]
        visited = set()
        minCost = {}

        while heap:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)
            minCost[node] = cost      # first pop = shortest path ✅

            for neighbor, weight in adjL[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor))

        return max(minCost.values()) if len(minCost) == n else -1