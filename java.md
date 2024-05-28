1st

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int OBSTACLE = 1;
        int SPACE = 0;
        int numRows = obstacleGrid.length;
        int numCols = obstacleGrid[0].length;

        int[][] numWays = new int[numRows][numCols];
        for (int row = 0; row < numRows; row++) {
            for (int col = 0; col < numCols; col++) {
                if (obstacleGrid[row][col] == OBSTACLE) {
                    continue;
                }
                if (row == 0 && col == 0) {
                    numWays[0][0] = 1;
                    continue;
                }
                if (row > 0) {
                    numWays[row][col] += numWays[row - 1][col];
                }
                if (col > 0) {
                    numWays[row][col] += numWays[row][col - 1];
                }
            }
        }
        return numWays[numRows - 1][numCols - 1];
    }
}
```
