// Time Complexity: O(n)
// Space Complexity: O(1) since we are using fixed size arrays for lowercase and uppercase characters.

class Solution {
    public int numberOfSpecialChars(String word) {


        HashSet<Character> lower = new HashSet<>();
        HashSet<Character> invalid = new HashSet<>();
        HashSet<Character> special = new HashSet<>();

        for(char ch : word.toCharArray()) {

            if(Character.isLowerCase(ch)) {

                if(invalid.contains(ch)) {
                    special.remove(ch);
                }

                lower.add(ch);

            } else {

                char small = Character.toLowerCase(ch);

                if(lower.contains(small) &&
                   !invalid.contains(small)) {

                    special.add(small);
                }

                invalid.add(small);
            }
        }

        return special.size();
    }
}