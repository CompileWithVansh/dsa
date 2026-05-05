//time complexity: O(n) where n is the length of the strings
//space complexity: O(1) since the frequency array is of fixed size (26 for

class Solution {
    public boolean isAnagram(String s, String t) {

        // Step 1: Length check
        if (s.length() != t.length()) {
            return false;
        }

        // Step 2: Frequency array for 'a' to 'z'
        int[] freq = new int[26];

        // Step 3: Count characters
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
            freq[t.charAt(i) - 'a']--;
        }

        // Step 4: Verify all counts are zero
        for (int count : freq) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
}