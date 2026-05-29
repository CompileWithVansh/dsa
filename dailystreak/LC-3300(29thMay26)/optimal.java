// Time Complexity: O(n × d) where d is the number of digits in the largest number. Since d ≤ 5, it simplifies to O(n).

// Space Complexity: O(1) because no extra data structures are used.


class Solution {
    public int minElement(int[] nums) {
        int min = Integer.MAX_VALUE;

        for (int num : nums) {
            int sum = 0;

            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }

            min = Math.min(min, sum);
        }

        return min;
    }
}