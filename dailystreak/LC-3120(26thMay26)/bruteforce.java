class Solution {
    public int numberOfSpecialChars(String word) {

        int count = 0;

        for(char ch = 'a'; ch <= 'z'; ch++) {

            if(word.contains(ch + "") &&
               word.contains((char)(ch - 32) + "")) {

                count++;
            }
        }

        return count;
    }
}