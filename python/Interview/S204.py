import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        mark = [True] * n
        mark[0] = False
        mark[1] = False
        for i in list(range(2, math.sqrt(n) + 1)):
            for j in list(range(2, math.sqrt(n) + 1)):
                







if __name__ == '__main__':
    print(Solution().countPrimes(100))