from _heapq import heapify
import collections
import queue

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.size = 0
        
    def addNum(self, num: int) -> None:
        # before adding, check maxheap and minheap and decide the heap
        # push to the heap
        # if the sizes differ by 2 adjust
        if self.size == 0 or num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
            self.size += 1
        else:
            heapq.heappush(self.maxheap, -num)
            self.size += 1
        
        if (len(self.minheap) - len(self.maxheap) > 1):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        elif (len(self.maxheap) - len(self.minheap)) > 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)
        print("minheap:", self.minheap)
        print("maxheap:",  self.maxheap)

    def findMedian(self) -> float:
        if (self.size % 2 != 0):
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            else:
                return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0])/2
        