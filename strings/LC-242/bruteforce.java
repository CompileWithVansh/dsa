//time complexity: O(n log n) where n is the length of the strings
//space complexity: O(n) due to the character arrays created from the strings
import java.util.Arrays;
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        char [] a = s.toCharArray();
        char [] b = t.toCharArray();

        Arrays.sort(a);
        Arrays.sort(b);

        return Arrays.equals(a,b);
    }
}