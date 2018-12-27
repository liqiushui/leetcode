class Solution:

    def __init__(self):
        self.path = 0

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) > 1 or len(obstacleGrid[0]) > 1:
            self.uniquePathsWithObstaclesPath(obstacleGrid, 0, 0)
        return s.path

    def uniquePathsWithObstaclesPath(self, obstacleGrid, pos_x, pos_y):

        if pos_x == len(obstacleGrid) - 1 and pos_y == len(obstacleGrid[0]) - 1:
            self.path += 1
            return

        if pos_x < len(obstacleGrid) and pos_y < len(obstacleGrid[0]) and obstacleGrid[pos_x][pos_y] > 0:
            return
        if pos_x < len(obstacleGrid):
            self.uniquePathsWithObstaclesPath(obstacleGrid, pos_x + 1, pos_y)

        if pos_y < len(obstacleGrid[0]):
            self.uniquePathsWithObstaclesPath(obstacleGrid, pos_x , pos_y + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))