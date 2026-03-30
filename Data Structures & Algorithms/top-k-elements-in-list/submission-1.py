class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency of each element
        # 1. map of frequency counters with num: freq
        # 2. dict.values() and sort them [3, 2, 1]

        count = Counter(nums)
        heap = []
        for i, c in count.items():
            heapq.heappush(heap, (-c, i))

        res=[]
        while(len(res) < k):
            res.append(heapq.heappop(heap)[1])
        return res