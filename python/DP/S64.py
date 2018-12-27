class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]

        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, col):
            dp[0][i] = dp[0][i-1] + grid[0][i]


        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])

        print(dp)

        return dp[-1][-1]



if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))