class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if not nums:
            return ret
        nums = sorted(nums)
        self.helper(nums, ret, [], 0)
        return ret

    def helper(self, nums, result, temp, pos):
        result.append(list(temp))
        i = pos
        while i < len(nums):
            temp.append(nums[i])
            self.helper(nums, result, temp, i + 1)
            temp.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))