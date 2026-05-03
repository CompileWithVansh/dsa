// Time complexity: O(n) due to string concatenation and substring search using contains().
// Space complexity: O(n) for the new concatenated string.
class Solution {
    public boolean rotateString(String s, String goal) {
        
        if (s.length() != goal.length()) {
            return false;
        }

        return (s + s).contains(goal);
    }
}
    