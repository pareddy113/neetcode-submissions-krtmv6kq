class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number in nums
        # Use a dictionary to store the count for each unique number
        count = Counter(nums)
        heap = []
        for num, i in count.items():
            heapq.heappush(heap, [-1*i, num])

        res = []

        while (len(res) < k):
            res.append(heapq.heappop(heap)[1])
        return res