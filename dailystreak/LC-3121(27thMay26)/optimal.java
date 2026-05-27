//time complexity: O(n) where n is the length of the input string
//space complexity: O(1) since we are using fixed size arrays


class Solution {
    public int numberOfSpecialChars(String word) {


        int[] lower = new int[26];
        int[] upper = new int[26];

        for(int i = 0; i < 26; i++) {
            lower[i] = -1;
            upper[i] = -1;
        }

        for(int i = 0; i < word.length(); i++) {

            char ch = word.charAt(i);

            if(Character.isLowerCase(ch)) {
                lower[ch - 'a'] = i; // last lowercase
            }
            else if(upper[ch - 'A'] == -1) {
                upper[ch - 'A'] = i; // first uppercase
            }
        }

        int count = 0;

        for(int i = 0; i < 26; i++) {

            if(lower[i] != -1 &&
               upper[i] != -1 &&
               lower[i] < upper[i]) {

                count++;
            }
        }

        return count;
    }
}