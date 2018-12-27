class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        length = rows * cols
        left = 0
        right = length - 1
        while left <= right:
            mid = int((left + right)/2)
            midValue = self.getElement(matrix, mid)
            if midValue == target:
                return True
            elif midValue > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def getElement(self, matrix, index):
        if not matrix:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        length = rows * cols

        if index < length:
            return matrix[int(index/cols)][int(index%cols)]
        return None


if __name__ == "__main__":
    s = Solution()
    matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
    print(s.searchMatrix(matrix, 50))
