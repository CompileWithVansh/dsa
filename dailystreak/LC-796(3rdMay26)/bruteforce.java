class Solution {
    // Time complexity: O(n^2) in the worst case, due to n rotations each requiring O(n) string operations.
    // Space complexity: O(n) auxiliary space, since new strings of length n are created during rotation.
    public boolean rotateString(String s, String goal) {
        
        for (int i = 0; i < s.length(); i++) {

            if (s.equals(goal)) {
                return true;
            } 
            else {
                s = s.substring(1) + s.substring(0, 1);
            }
        }

        return false;
        
    }
}


