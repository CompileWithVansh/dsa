class Solution {
    // Time complexity: O(n), Space complexity: O(n)
    // Optimal solution using StringBuilder as a stack but both solution are working same concept of stack
    public String removeDuplicates(String s) {
        StringBuilder sb = new StringBuilder();

        for (char ch : s.toCharArray()) {
            int len = sb.length();
            if (len > 0 && sb.charAt(len - 1) == ch) {
                sb.deleteCharAt(len - 1);
            } else {
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}