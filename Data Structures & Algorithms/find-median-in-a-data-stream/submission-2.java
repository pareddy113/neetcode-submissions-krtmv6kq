class MedianFinder {

    private PriorityQueue<Integer> smallMaxHeap;
    private PriorityQueue<Integer> largeMinHeap;

    public MedianFinder() {
        this.smallMaxHeap = new PriorityQueue<Integer>((a,b) -> b - a);
        this.largeMinHeap = new PriorityQueue<Integer>((a,b) -> a - b);
    }
    
    public void addNum(int num) {
        // If either of them emtpy, we can add it to small so its sorted
        if (smallMaxHeap.isEmpty() || largeMinHeap.isEmpty()) {
            smallMaxHeap.add(num);
        } else {
            int maxHeapMaxValue = smallMaxHeap.peek();
            int minHeapMinValue = largeMinHeap.peek();

            if (num > maxHeapMaxValue) {
                largeMinHeap.add(num);
            } else {
                smallMaxHeap.add(num);
            }
        }

        // rebalancing
        if (Math.abs((smallMaxHeap.size() - largeMinHeap.size())) > 1) {
            if (smallMaxHeap.size() > largeMinHeap.size()) {
            int val = smallMaxHeap.poll();
            largeMinHeap.offer(val);
        } else {
            int val = largeMinHeap.poll();
            smallMaxHeap.offer(val);
        }
    }
    }
    
    public double findMedian() {
        int size = smallMaxHeap.size() + largeMinHeap.size();
        // TODO: edge case

        if (size%2 == 0) {
            return (smallMaxHeap.peek() + largeMinHeap.peek())/2.0;
        } else {
            if (smallMaxHeap.size() > largeMinHeap.size()) return smallMaxHeap.peek();
            else return largeMinHeap.peek();
        }

    }
}
