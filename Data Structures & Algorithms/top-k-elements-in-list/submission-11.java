class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
    /*
        given: nums, k
        output: K most frequent elements in the array, any order
        Algorithm:
            - calculate freq of num O(n)
            - return top k
                - min heap of size k and pop out all elements > k O(n) int[freq, val]

        TC: O(n)
        SC: O(n)
    */ 

    Map<Integer, Integer> freq = new HashMap<>();
    PriorityQueue<int[]> minHeap = new PriorityQueue<>((a,b) -> Integer.compare(a[0],b[0]));

    for(int num: nums) {
        freq.put(num, freq.getOrDefault(num, 0) + 1);
    }

    for(Map.Entry<Integer, Integer> entry: freq.entrySet()) {
        minHeap.offer(new int[]{entry.getValue(), entry.getKey()});

        if (minHeap.size() > k) {
            minHeap.poll();
        }
    }

    int[] output = new int[k];
    for(int i = 0; i <k; i++) {
        output[i] = minHeap.poll()[1];
    }
    return output;
    }
}
