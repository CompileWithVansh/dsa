// Time Complexity: O(n^2) - nested loops iterate over all pairs
// Space Complexity: O(1) - no extra data structures used

class Solution {
    public int[] twoSum(int[] nums, int target) {
        

        for(int i =0;i<nums.length;i++){
            for(int j =i+1;j<nums.length;j++){
                

                if (nums[i]+nums[j]==target){
                    return new int[]{i,j};

                }
            }
        }
        return new int[]{-1,-1};
        
    }

}