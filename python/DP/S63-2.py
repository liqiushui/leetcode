class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, row):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])

        for i in range(1, col):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])


        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])*(1 - obstacleGrid[i][j])

        return dp[-1][-1]



if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))