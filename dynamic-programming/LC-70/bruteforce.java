// using recursion to solve this problem but it give tle 
//not suggested to do just for understanding the problem
//time complexity: O(2^n) - each call to climbStairs results in two additional calls
//space complexity: O(n) - the maximum depth of the recursion tree can be n
class Solution {
    
    public int climbStairs(int n) {
        
        if (n == 1) {
            return 1;
        }

        if (n == 2) {
            return 2;
        }

        return climbStairs(n - 1) + climbStairs(n - 2);
    }
}