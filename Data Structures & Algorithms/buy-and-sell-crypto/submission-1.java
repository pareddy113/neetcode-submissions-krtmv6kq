class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices.length > 0 ? prices[0] : 0;
        int maxProfit = 0;

        // Init 10, 0
        // 1 1 1 0
        // 2 5 1 4
        // 3 6 1 5
        for(int i = 1; i < prices.length; i++) {
            // lowest price yet
            minPrice = Math.min(minPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);       
        }
        return maxProfit;
    }
}
