//time complexity: O(n*m*min(len(s1), len(s2))) where n and m are the lengths of arr1 and arr2 respectively, and len(s1) and len(s2) are the lengths of the string representations of the integers in arr1 and arr2
//space complexity: O(1) as we are using only a constant amount of extra space

class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {

        int ans = 0;

        for (int a : arr1) {

            for (int b : arr2) {

                String s1 = String.valueOf(a);
                String s2 = String.valueOf(b);

                int len = Math.min(s1.length(), s2.length());

                int count = 0;

                for (int i = 0; i < len; i++) {

                    if (s1.charAt(i) == s2.charAt(i)) {
                        count++;
                    } else {
                        break;
                    }
                }

                ans = Math.max(ans, count);
            }
        }

        return ans;
    }
}