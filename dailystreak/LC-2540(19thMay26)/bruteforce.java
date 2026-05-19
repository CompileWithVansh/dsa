//time complexity: O(m*n) where m and n are the lengths of the two input arrays
//space complexity: O(1) as we are using only constant extra space
//brute force approach: we iterate through each element of the first array and compare it
class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    return nums1[i];
                }
            }
        }
        return -1;
    }
}