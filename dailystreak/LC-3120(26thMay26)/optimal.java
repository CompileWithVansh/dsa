// Time Complexity
// O(n)
// Space Complexity
// O(52)≈O(1)
// Because only English letters are stored.

class Solution {
    public int numberOfSpecialChars(String word) {

        HashSet<Character> set = new HashSet<>();

        for(char ch : word.toCharArray()) {
            set.add(ch);
        }

        int count = 0;

        for(char ch = 'a'; ch <= 'z'; ch++) {

            if(set.contains(ch) &&
               set.contains(Character.toUpperCase(ch))) {

                count++;
            }
        }

        return count;
    }
}