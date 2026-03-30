class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length - 1;
        int maxArea = 0;

        while (l < r) {
            System.out.println(l + "  " + r);
            int minHeight = Math.min(heights[l], heights[r]);
            maxArea = Math.max(maxArea, (r - l) * minHeight);
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
       return maxArea;
    }
}
