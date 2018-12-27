class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums)
        t = 0
        for x in range(len(nums)):
            i = i ^ x
            t = t ^ nums[x]
        return i ^ t





if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))