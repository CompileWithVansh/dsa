/*
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
class Solution {

    //used fibonaci series to solve this problem
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }

        int first = 1;
        int second = 2;

        for (int i = 3; i <= n; i++) {

            int current = first + second;

            first = second;
            second = current;
        }

        return second;

    }
}