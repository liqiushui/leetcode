class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result = result ^ i
        return result



if __name__ == '__main__':

    s = Solution()
    print(s.singleNumber([1,1,3,3,7,8,8,7,5]))