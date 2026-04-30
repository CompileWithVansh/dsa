//using hashmap in java \

// Time Complexity: O(n) - single pass through the array
// Space Complexity: O(n) - HashMap stores at most n elements

import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer>ourhashmap = new HashMap<>();

        for(int i =0;i<nums.length;i++){
            int value=nums[i];
            int moreNeeded= target - value;
            if (ourhashmap.containsKey(moreNeeded)){
                return new int[]{ourhashmap.get(moreNeeded) , i};

            }
            ourhashmap.put(value,i);
            
        }
        return new int[]{-1,-1};
        
    }
}