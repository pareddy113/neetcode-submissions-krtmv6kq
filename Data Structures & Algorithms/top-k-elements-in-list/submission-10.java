class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // [1,1,2,2,3,3,3]
        // 1: [1,1], 2:[2,2], 3:[3,3] O(n logn)

        // sort nums, push to max heap (freq, num)
        // ArrayList, LinkedList, HashSet, HashMap, ArrayDeque, LinkedHashMap, TreeMap, TreeSet

        PriorityQueue<int[]> heap = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        
        for (int i: nums) {
            Integer count = freqMap.getOrDefault(i, 0);
            freqMap.put(i, count + 1);
        }
        
        for(Map.Entry<Integer, Integer> key: freqMap.entrySet()) {
            heap.add(new int[]{key.getValue(), key.getKey()});
            if (heap.size() > k) {
                heap.poll();
            }
        }
        
        int[] output = new int[k];
        int i = 0;
        while(i < k) {
            output[i] = heap.poll()[1];
            i++;
        }
        return output;
    }
}
