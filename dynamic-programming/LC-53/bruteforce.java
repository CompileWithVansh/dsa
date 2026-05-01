class Solution {
    public int maxSubArray(int[] nums) {
        // Time Complexity: O(n^2)
        // Space Complexity: O(1)
        int maximum = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {

            int sum = 0;

            for (int j = i; j < nums.length; j++) {

                sum += nums[j];

                if (sum > maximum) {
                    maximum = sum;
                }
            }
        }

        return maximum;
    }
}