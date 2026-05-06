//time complexity - o(m*n)
//space complexity - o(m*n) because of rotating list 
class Solution {
    public char[][] rotateTheBox(char[][] boxGrid) {

        int m = boxGrid.length;
        int n = boxGrid[0].length;

        // Move stones towards right due to gravity
        for (int i = 0; i < m; i++) {

            // position where next stone should go
            int empty = n - 1;

            // traverse from right to left
            for (int j = n - 1; j >= 0; j--) {

                // obstacle found
                if (boxGrid[i][j] == '*') {

                    empty = j - 1;
                }

                // stone found
                else if (boxGrid[i][j] == '#') {

                    // move stone to empty position
                    char temp = boxGrid[i][empty];
                    boxGrid[i][empty] = '#';
                    boxGrid[i][j] = temp;

                    // next empty position shifts left
                    empty--;
                }
            }
        }

        // Rotate matrix m*n - n*m
        char[][] ans = new char[n][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                ans[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        return ans;
    }
}