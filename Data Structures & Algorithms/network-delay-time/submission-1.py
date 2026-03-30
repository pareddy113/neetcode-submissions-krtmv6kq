class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
        
        # adjL = defaultdict(list)
        # for s,t,c in times:
        #     adjL[s].append([t,c])
        
        # visiting = set()

        # # 1: [[2,1],[4,4]]
        # # 2:[[3,1]]
        # # 3: [[4,1]]

        # # s=1, c=0 visiting= [1]
        # # s=2, c=1 visiting= [1,2]

        # print(adjL)
        
        # minCost = { i: float("inf") for i in range(1, n+1)}
        # minCost[k] = 0
        # def dfs(s, c):            
        #     for target, cost in adjL[s]:
        #         nc = c + cost
        #         if nc < minCost[target]:
        #             print(nc, minCost, target)
        #             minCost[target] = nc
        #             dfs(target, nc)
        

        # dfs(k, 0)
        # minDist = max(minCost.values())
        # return -1 if minDist == float("inf") else minDist
