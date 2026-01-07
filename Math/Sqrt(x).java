class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;

        int left = 1;
        int right = Math.min(x / 2, 46340); // 46340^2 <= Integer.MAX_VALUE
        int ans = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (mid <= x / mid) { 
                ans = mid;          
                left = mid + 1;
            } else {
                right = mid - 1;  
            }
        }
        return ans;
    }
}
