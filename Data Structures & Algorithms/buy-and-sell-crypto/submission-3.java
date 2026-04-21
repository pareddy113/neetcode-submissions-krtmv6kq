class Solution {
    public int maxProfit(int[] prices) {
        
        int minValue = Integer.MAX_VALUE;        
        int maxProfit = 0;

        for(int price: prices) {
            
            minValue = Math.min(minValue, price);
            maxProfit = Math.max(maxProfit, price - minValue);
        }
        return maxProfit;
    }
}
