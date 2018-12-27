class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num = None
        max_num = None
        for x in nums:
            if min_num == None or x <= min_num:
                min_num = x
            elif max_num == None or x <= max_num:
                max_num = x
            else:
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([2,1,5,0,3,4]))