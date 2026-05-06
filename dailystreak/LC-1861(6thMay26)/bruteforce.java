/* 
just for idea not for study and submission 
time complexity: O(m*n) for rotation and O(m*n) for gravity, overall O(m*n)
time complexity in worst case - O(m*n*n) because of nested while loop for gravity
space complexity - O(m*n) because of rotating list
this is brute force approach, we first rotate the matrix and then apply gravity to move the stones downwards. We check for each stone and move it down until it is blocked by an obstacle or another stone.       
*/

class Solution {
    public char[][] rotateTheBox(char[][] boxGrid) {

        int m = boxGrid.length;
        int n = boxGrid[0].length;

        // Step 1: Rotate matrix
        char[][] rotated = new char[n][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                rotated[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        // Step 2: Apply gravity
        for (int col = 0; col < m; col++) {

            // move from bottom upwards
            for (int row = n - 1; row >= 0; row--) {

                // if stone found
                if (rotated[row][col] == '#') {

                    int curr = row;

                    // move stone downward until blocked
                    while (curr + 1 < n &&
                           rotated[curr + 1][col] == '.') {

                        rotated[curr + 1][col] = '#';
                        rotated[curr][col] = '.';

                        curr++;
                    }
                }
            }
        }

        return rotated;
    }
}