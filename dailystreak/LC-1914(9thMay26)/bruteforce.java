// Approach:
// Rotate each layer one step at a time in counter-clockwise direction
// Repeat the same rotation k times for every layer

// TC: O(k * m * n)
// SC: O(1)

class Solution {

    public int[][] rotateGrid(int[][] grid, int k) {

        int m = grid.length;
        int n = grid[0].length;

        int layers = Math.min(m, n) / 2;

        for (int layer = 0; layer < layers; layer++) {

            int top = layer;
            int left = layer;

            int bottom = m - layer - 1;
            int right = n - layer - 1;

            for (int step = 0; step < k; step++) {

                int first = grid[top][left];

                for (int j = left; j < right; j++) {
                    grid[top][j] = grid[top][j + 1];
                }

                for (int i = top; i < bottom; i++) {
                    grid[i][right] = grid[i + 1][right];
                }

                for (int j = right; j > left; j--) {
                    grid[bottom][j] = grid[bottom][j - 1];
                }

                for (int i = bottom; i > top + 1; i--) {
                    grid[i][left] = grid[i - 1][left];
                }

                grid[top + 1][left] = first;
            }
        }

        return grid;
    }
}