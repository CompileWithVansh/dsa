//time complexity: O(nlogn) due to sorting
//space complexity: O(1)

class Solution {
    public boolean isGood(int[] nums) {
        
        Arrays.sort(nums);

        int n = nums[nums.length - 1];

        // Length should be n + 1
        if (nums.length != n + 1) {
            return false;
        }

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] != i + 1) {
                return false;
            }
        }

        // Last two elements should be n
        return nums[n - 1] == n && nums[n] == n;
    }
}