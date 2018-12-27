class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [[-1]*n for i in range(n)]

        left = 0
        right = n-1
        up = 0
        bottom = n-1
        step = 1

        row = 0
        col = 0

        while left < right and up < bottom:

            for col in range(left, right + 1):
                m[row][col] = step
                step += 1
            up += 1

            for row in range(up, bottom + 1):
                m[row][col] = step
                step += 1

            right -= 1
            for col in range(right, left - 1, -1):
                m[row][col] = step
                step += 1

            bottom -= 1
            for row in range(bottom, up - 1, -1):
                m[row][col] = step
                step += 1
            left += 1

        if n%2 == 1:
            m[int(n/2)][int(n/2)] = n**2

        return m




if __name__ == '__main__':
    s = Solution()
    m = s.generateMatrix(7)
    for r in range(len(m)):
        for c in range(len(m[0])):
            print(str(m[r][c]) + " " , end="")
        print()
