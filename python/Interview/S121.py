class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_last = 2**32-1
        result = 0
        for i in prices:
            min_last = min(min_last, i)
            result = max(result, i - min_last)

        return result



if __name__ == '__main__':
    print(Solution().maxProfit([7,6,4,3,1]))




