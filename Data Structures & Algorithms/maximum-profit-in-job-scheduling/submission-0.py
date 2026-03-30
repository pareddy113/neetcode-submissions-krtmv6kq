class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        max_profit=0
        heap=[]
        items=sorted(zip(startTime,endTime,profit))

        for start,end,profit in items:
            while heap and start>=heap[0][0]:
                max_profit=max(max_profit,heap[0][1])
                heapq.heappop(heap)
            heapq.heappush(heap,(end,max_profit+profit))
        
        while heap:
            max_profit=max(max_profit,heap[0][1])
            heapq.heappop(heap)
        return max_profit