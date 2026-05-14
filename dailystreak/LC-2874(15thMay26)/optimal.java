//time complexity: O(n)
//space complexity: O(n)

class Solution {
    public boolean isGood(int[] nums) {

        int n = nums.length - 1;

        int[] freq = new int[n + 1];

        for (int num : nums) {

            // Number should be between 1 and n
            if (num < 1 || num > n) {
                return false;
            }

            freq[num]++;
        }

        // 1 to n-1 should appear exactly once
        for (int i = 1; i < n; i++) {
            if (freq[i] != 1) {
                return false;
            }
        }

        // n should appear exactly twice
        return freq[n] == 2;
    }
}


//try 2
//time complexity: O(n)
//space complexity: O(1)

class Solution {
    public boolean isGood(int[] nums) {

        int n = nums.length - 1;

        int duplicate = -1;

        for (int i = 0; i < nums.length; i++) {

            int val = Math.abs(nums[i]);

            // value must be between 1 and n
            if (val < 1 || val > n) {
                return false;
            }

            int idx = val - 1;

            if (nums[idx] < 0) {

                // only n can repeat
                if (val != n || duplicate != -1) {
                    return false;
                }

                duplicate = val;

            } else {
                nums[idx] *= -1;
            }
        }

        return duplicate == n;
    }
}