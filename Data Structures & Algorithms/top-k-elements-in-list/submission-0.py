class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency of each element
        # 1. map of frequency counters with num: freq
        # 2. dict.values() and sort them [3, 2, 1]

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), count.get)