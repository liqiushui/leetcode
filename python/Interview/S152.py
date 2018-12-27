class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last_sub_min = nums[0]
        last_sub_max = last_sub_min
        sub_max = last_sub_min

        for i in range(1, len(nums)):
            max_pre = last_sub_max
            last_sub_max = max(max(nums[i] * max_pre, nums[i]), last_sub_min * nums[i])
            last_sub_min = min(min(nums[i] * last_sub_min, nums[i]), max_pre * nums[i])
            sub_max = max(last_sub_max, sub_max)
        return sub_max



if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-4,-3,-2]))