class Solution {
    public int maxProfit(int[] prices) {
        int l = 0, r = l + 1;
        int max = 0;
        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                int temp = prices[r] - prices[l];
                max = Math.max(max, temp);
            } else {
                l = r;
            }
            r++;
        }
        return max;
    }
}
