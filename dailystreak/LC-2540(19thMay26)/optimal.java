//time complexity: O(m+n) where m and n are the lengths of the two input arrays
//space complexity: O(1) as we are using only constant extra space
//two pointer approach: we initialize two pointers, one for each array, and compare the elements at those pointers. 

class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int i = 0, j = 0;

        while (i < nums1.length && j < nums2.length) {

            if (nums1[i] == nums2[j]) {
                return nums1[i];
            }

            if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
            }
        }

        return -1;
    }
}