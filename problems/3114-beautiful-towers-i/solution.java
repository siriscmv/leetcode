class Solution {
    public long maximumSumOfHeights(List<Integer> maxHeights) {
        int i = 0, j = 0;
        long ans = 0, mx = 0, sum = 0, init = 0;
        int len = maxHeights.size();

        for (i = 0; i < len; i++) {
            init = maxHeights.get(i);
            sum = init; 
            
            for (j = i-1, mx = init; j >= 0; j--) {
                mx = Math.min(mx, maxHeights.get(j));
                sum += mx;
            }

            for (j = i+1, mx = init; j < len; j++) {
                mx = Math.min(mx, maxHeights.get(j));
                sum += mx;
            }

            ans = Math.max(ans, sum);
        }

        return ans;
    }
}
